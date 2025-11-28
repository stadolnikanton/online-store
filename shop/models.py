from django.db import models


class ProductType(models.Model):
    title = models.CharField()

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    name = models.CharField(verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(verbose_name="Количество товаров")
    product_types = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_img", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
