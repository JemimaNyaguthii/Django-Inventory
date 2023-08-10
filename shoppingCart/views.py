from django.shortcuts import render
from django.shortcuts import render, redirect
from inventory.models import Product 
from .models import CartItem
from .forms import CartItemForm 

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.product = product
            cart_item.save()
            return redirect("cart_view")
    else:
        form = CartItemForm()
    return render(request, "add_to_cart.html", {"form": form, "product": product})

def cart_view(request):
    cart_items = CartItem.objects.all()
    return render(request, "cart_view.html", {"cart_items": cart_items})

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect("cart_view")
