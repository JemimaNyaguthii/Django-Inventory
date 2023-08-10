from django.shortcuts import render
from django.shortcuts import render
from .forms import OrderUploadForm
from inventory.models import Product
from django.shortcuts import render,redirect


# Create your views here.
def order_upload_view(request):
    if request.method=="POST":
        form= OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=OrderUploadForm
    return render (request,"order_upload.html",{"form":form})

def order_list(request):
    orders=Order.objects.all()
    return render (request,"order_list.html",{"products":products})


def order_detail(request,id):
    orders=Order.objects.get(id=id)
    return render(request,"order_detail.html",{"product":product})   

def order_update_view(request,id):
    product=Order.objects.get() 
    if request.method =="POST":
        form = OrderUploadForm(request.POST,instance=product)
        if form_is_valid():
            form.save()
        return redirect("order_detail_view", id=product.id)   
    else:
        form =OrderUploadForm(instance=product)
    return render(request,"inventory/edit_order",{"form".form}) 

def delete_order(request,id):
    order=Order.objects.get(id=id) 
    order.delete()
    return redirect("order_list_view")
  