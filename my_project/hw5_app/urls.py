from django.urls import path
from hw5_app.apps import Hw5AppConfig

from . import views

app_name = Hw5AppConfig.name


urlpatterns = [
    path("clients/", views.AllClientView.as_view(), name="all_clients"),
    path("products/", views.AllProductsView.as_view(), name="all_products"),
    path(
        "orders/client/<int:client_id>/",
        views.ClientOrdersView.as_view(),
        name="client_orders",
    ),
    path(
        "products/client/<int:client_id>/",
        views.ClientProductsView.as_view(),
        name="client_products",
    ),
    path(
        "product/create/client/<int:client_id>/",
        views.CreateProductView.as_view(),
        name="create_product",
    ),
    path(
        "product/<int:product_id>/update/client/<int:client_id>/",
        views.UpdateProductView.as_view(),
        name="update_product",
    ),
]
