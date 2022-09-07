from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_book_list, name="home"),
    path("detail/<int:pk>", views.show_book_detail, name="detail"),
    path("cart_add/<int:pk>", views.add_to_cart, name="cart"),
    path("show_cart/",views.CartView.as_view(), name='show_cart')
    
    #path("order_add", views.add_to_order, name="order"),

]
