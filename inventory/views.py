from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import render,redirect


# Create your views here.
def product_upload_view(request):
    if request.method=="POST":
        form= ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProductUploadForm
    return render (request,"product_upload.html",{"form":form})

def products_list(request):
    products=Product.objects.all()
    return render (request,"product_list.html",{"products":products})


def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"product_detail.html",{"product":product})   

def product_update_view(request,id):
    product=Product.objects.get() 
    if request.method =="POST":
        form = ProductUploadForm(request.POST,instance=product)
        if form_is_valid():
            form.save()
        return redirect("product_detail_view", id=product.id)   
    else:
        form =ProductUploadForm(instance=product)
    return render(request,"inventory/edit_product",{"form".form}) 

def delete_product(request,id):
    product=Product.objects.get(id=id) 
    product.delete()
    return redirect("product_list_view")
  
