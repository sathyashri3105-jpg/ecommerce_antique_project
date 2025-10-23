from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from products.models import Product

@login_required(login_url='login') 
def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        products.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })
        total += product.price * quantity

    return render(request, 'cart/detail.html', {'products': products, 'total': total})


@login_required(login_url='login')
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('cart-detail')

@login_required(login_url='login')
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('cart-detail')


@login_required(login_url='login') 
def checkout(request):
    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        return render(request, "cart/checkout_success.html", {"payment_method": payment_method})
    return render(request, "cart/checkout.html")