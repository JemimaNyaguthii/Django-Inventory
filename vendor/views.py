# from django.shortcuts import render,redirect
# from .forms import VendorForm
# from .models import Vendor

# def vendor_create_view(request):
#     if request.method == "POST":
#         form = VendorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("vendor_list_view")
#     else:
#         form = VendorForm()
#     return render(request, "vendor_create.html", {"form": form})

# def vendor_list(request):
#     vendors = Vendor.objects.all()
#     return render(request, "vendor_list.html", {"vendors": vendors})

# def vendor_detail(request, id):
#     vendor = Vendor.objects.get(id=id)
#     return render(request, "vendor_detail.html", {"vendor": vendor})

# def vendor_update_view(request, id):
#     vendor = Vendor.objects.get(id=id)
#     if request.method == "POST":
#         form = VendorForm(request.POST, instance=vendor)
#         if form.is_valid():
#             form.save()
#             return redirect("vendor_detail_view", id=vendor.id)
#     else:
#         form = VendorForm(instance=vendor)
#     return render(request, "vendor_update.html", {"form": form})

# def delete_vendor(request, id):
#     vendor = Vendor.objects.get(id=id)
#     vendor.delete()
#     return redirect("vendor_list_view")
from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm 

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

def upload_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor-list')
    else:
        form = VendorForm()
    return render(request, 'vendor/upload_vendor.html', {'form': form})

def edit_vendor(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor-list')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor/edit_vendor.html', {'form': form, 'vendor': vendor})

def delete_vendor(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor-list')
    return render(request, 'vendor/delete_vendor.html', {'vendor': vendor})
