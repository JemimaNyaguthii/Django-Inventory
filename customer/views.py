from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomerUploadForm
from .models import Customer

# Create your views here.
def customer_upload_view(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list_view")
    else:
        form = CustomerUploadForm()
    return render(request, "customer_detail_view.html", {"form": form})

def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, "customer_list_view.html", {"customers": customers})

def customer_detail_view(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer_detail_view.html", {"customer": customer})

def customer_update_view(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_detail_view", id=customer.id)
    else:
        form = CustomerUploadForm(instance=customer)
    return render(request, "customer_update.html", {"form": form})

def delete_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("customer_list_view")


