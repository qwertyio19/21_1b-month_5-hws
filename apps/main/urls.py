from django.urls import path
from apps.main.views import CreateSettingsView, CreateMainView, CreateOverSerializer, CreateUserSerializer, CreateProductSerializer, CreateOrderSerializer, CreateBlogPostSerializer

urlpatterns = [
    path('settings/create/', CreateSettingsView.as_view(), name="settings_create"),
    path('main/create/', CreateMainView.as_view(), name="main_create"),
    path('over/create/', CreateOverSerializer.as_view(), name="over_create"),
    path('user/create/', CreateUserSerializer.as_view(), name = "user_create"),
    path('product/create/', CreateProductSerializer.as_view(), name="product_create"), 
    path('order/create/', CreateOrderSerializer.as_view(), name="order_create"), 
    path('blogpost/create/', CreateBlogPostSerializer.as_view(), name="blogpost_create"),
]

