from django.urls import path
from .views import cart_detail, add_to_cart, remove_from_cart, checkout

urlpatterns = [
    path('', cart_detail, name='cart-detail'),              # View cart
    path('add/<int:pk>/', add_to_cart, name='add-to-cart'), # Add product
    path('remove/<int:pk>/', remove_from_cart, name='remove-from-cart'),  # Remove product
    path('checkout/', checkout, name='checkout'),
]
