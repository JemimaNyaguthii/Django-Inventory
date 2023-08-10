from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DeliveryForm 
from inventory.models import Product
from .models import Delivery

# Create your views here.
def delivery_upload_view(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DeliveryForm()
    return render(request, "delivery_upload.html", {"form": form})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "delivery_list.html", {"deliveries": deliveries})

def delivery_detail(request, id):
    delivery = Delivery.objects.get(id=id)
    return render(request, "delivery_detail.html", {"delivery": delivery})

def delivery_update_view(request, id):
    delivery = Delivery.objects.get(id=id)
    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect("delivery_detail_view", id=delivery.id)
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, "inventory/edit_delivery.html", {"form": form})

def delete_delivery(request, id):
    delivery = Delivery.objects.get(id=id)
    delivery.delete()
    return redirect("delivery_list_view")