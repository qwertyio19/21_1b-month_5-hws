from django.contrib import admin
from apps.main.models import Settings, Main, Over, User, Product, Order, BlogPost

# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Over)
class OverAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title",)