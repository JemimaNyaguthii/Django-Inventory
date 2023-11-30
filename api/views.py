from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializer import CustomerSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request,id, format=None):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request,id, format=None):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id, format=None):
        customer = self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CartListView(APIView):
    def get(self,request):
        carts =Cart.objects.all()
        serializer =CartSerializer(carts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer =CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class AddToCartView(APIView):
    def post(self,request,format=None):
        cart_id =request.data["cart_id"]
        product_id = request.data["product_id"]
        cart =Cart.objects.get(id =cart_id)
        product =Product.objects.get(id =product_id)
        updated_cart =Cart.add_product(product)
        serializer = CartSerializer(updated_cart)
        return Response(serializer.data)

