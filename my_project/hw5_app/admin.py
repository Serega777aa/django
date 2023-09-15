from django.contrib import admin

from .models import Category, Client, Order, OrderItem, Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "registration_date")
    list_filter = ("registration_date",)
    search_fields = ("name", "email", "phone_number")
    date_hierarchy = "registration_date"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "added_date")
    list_filter = ("category", "added_date")
    search_fields = ("name", "description")
    date_hierarchy = "added_date"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "total_amount", "order_date")
    list_filter = ("order_date",)
    search_fields = ("client__name",)
    date_hierarchy = "order_date"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    list_filter = ("order",)
    search_fields = ("product__name",)

