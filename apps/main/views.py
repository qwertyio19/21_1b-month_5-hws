from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from apps.main.models import Settings, Main, Over, User, Product, Order, BlogPost, Products, ProductImage
from apps.main.serializer import SettingsSerializer, MainSerializer, OverSerializer, UserSerializer, ProductSerializer, OrderSerializer, BlogPostSerializer, ProductsSerializer


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


class ProductsCreateView(CreateAPIView):
    queryset = Products
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        product = serializer.save()

        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)


class ProductListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer