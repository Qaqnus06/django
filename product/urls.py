from django.urls import path
from .import views

app_name='product'
urlpatterns = [
    path('',views.ProductListView.as_view(), name='index'),
    path('category/<int:id>/',views.CategoryProductsList.as_view(),name='category'),
    path('about/<int:id>/',views.about,name='about') ,
    path('product_detail/<int:id>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('haqida/',views.haqida,name='haqida'),

    path('cart_summary/',views.cart_summary,name='cart_summary'),
    path('cart_add/',views.cart_add,name='cart_add'),
    path('cart_delete/',views.cart_delete,name='cart_delete'),
    path('cart_update/',views.cart_update,name='cart_update'),
]