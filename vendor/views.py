from django.shortcuts import render,redirect
from .forms import VendorForm
from .models import Vendor

def vendor_create_view(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendor_list_view")
    else:
        form = VendorForm()
    return render(request, "vendor_create.html", {"form": form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, "vendor_list.html", {"vendors": vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, "vendor_detail.html", {"vendor": vendor})

def vendor_update_view(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == "POST":
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail_view", id=vendor.id)
    else:
        form = VendorForm(instance=vendor)
    return render(request, "vendor_update.html", {"form": form})

def delete_vendor(request, id):
    vendor = Vendor.objects.get(id=id)
    vendor.delete()
    return redirect("vendor_list_view")
