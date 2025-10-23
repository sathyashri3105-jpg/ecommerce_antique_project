from django.shortcuts import render
from products.models import Product  # Import Product model

def home(request):
    featured_products = Product.objects.all()[:3]  # Get first 3 products
    return render(request, 'home/index.html', {'featured_products': featured_products})
