from django.urls import path
from .import views


urlpatterns = [
    path('sell/', views.sell, name='sell'),
    path('<int:pet_id>/', views.detail, name='detail'),
    path('<int:pet_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('<int:pet_id>/remove_from_cart', views.remove_from_cart, name='remove'),
    path('cart/', views.cart, name='cart')
]
