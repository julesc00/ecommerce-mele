
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """Add items to cart."""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd["quantity"],
                 override_quantity=cd["override"])

    return redirect("cart:cart_detail")


def cart_detail(request):
    """List items in the cart."""

    cart = Cart(request)
    context = {"cart": cart}
    return render(request, "cart/detail.html", context)


@require_POST
def cart_remove(request, product_id):
    """Remove items from cart."""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect("cart:cart_detail")
