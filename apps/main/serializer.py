from rest_framework import serializers
from apps.main.models import Settings, Main, Over, User, Product, Order, BlogPost, ProductImage, Products

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = "__all__"


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"


class OverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Over
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"  


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = ProductImage
        fields = ['image', 'position']
        
class ProductsSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'is_active', 'product_image', 'created_at']