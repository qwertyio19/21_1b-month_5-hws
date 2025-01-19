from rest_framework.generics import CreateAPIView
from apps.main.models import Settings, Main, Over, User, Product, Order, BlogPost
from apps.main.serializer import SettingsSerializer, MainSerializer, OverSerializer, UserSerializer, ProductSerializer, OrderSerializer, BlogPostSerializer


class CreateSettingsView(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


class CreateMainView(CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class CreateOverSerializer(CreateAPIView):
    queryset = Over.objects.all()
    serializer_class = OverSerializer


class CreateUserSerializer(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateProductSerializer(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateOrderSerializer(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateBlogPostSerializer(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer