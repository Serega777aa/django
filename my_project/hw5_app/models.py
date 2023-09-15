from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField()

    class Meta:
        verbose_name_plural = "Clients"

    def get_absolute_url(self):
        return reverse(
            "shop_app:client_orders",
            kwargs={"client_id": self.pk},
        )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField()
    photo = models.ImageField(upload_to="products/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders"
    )
    products = models.ManyToManyField(
        Product, through="OrderItem", related_name="orders"
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.pk} by {self.client}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.product} ({self.quantity} items)"
