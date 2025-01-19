from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    photo = models.ImageField(
        upload_to="photo/",
        verbose_name="Фото"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"


class Over(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Заголовок"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главные"


class User(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Имя"
    )

    age = models.IntegerField(
        verbose_name="Возраст"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название товата"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    stock = models.IntegerField(
        verbose_name="Запас"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Общая сумма"
    )

    status = models.CharField(
        max_length=50,
        verbose_name="Статус"
    )

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField()


class BlogPost(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    author = models.CharField(
        max_length=100,
        verbose_name="Автор"
    )

    content = models.TextField(
        verbose_name="Контент"
    )

    published_date = models.DateTimeField(
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост в блоге"
        verbose_name_plural = "Посты в блоге"