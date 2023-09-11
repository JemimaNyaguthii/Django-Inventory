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
    user = request.user
    cart_items = Cart.objects.filter(user=user).prefetch_related('products')
    total_price = sum(product.price * product.quantity for cart in cart_items for product in cart.products.all())
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect("cart_view")
