from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from hw5_app.forms import ProductForm
from hw5_app.models import Client, Order, Product


class HomeViews(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context


class AllClientView(ListView):
    model = Client
    template_name = "all_clients.html"
    context_object_name = "clients"

    def get_queryset(self):
        return Client.objects.all()


class AllProductsView(ListView):
    model = Product
    template_name = "all_products.html"
    context_object_name = "products"


class ClientOrdersView(ListView):
    model = Order
    template_name = "client_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        client_id = self.kwargs["client_id"]
        return Order.objects.filter(client_id=client_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get("client_id")
        client = Client.objects.get(pk=client_id)
        context["client"] = client
        return context


class ClientProductsView(ListView):
    model = Product
    template_name = "client_products.html"
    context_object_name = "products"

    def get_queryset(self):
        client_id = self.kwargs["client_id"]
        period = self.request.GET.get("period", "7")
        end_date = datetime.now()
        start_date = end_date - timedelta(days=int(period))

        products = Product.objects.filter(
            orders__client_id=client_id,
            orders__order_date__gte=start_date,
            orders__order_date__lte=end_date,
        ).distinct()

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        period = self.request.GET.get("period", "7")
        client_id = self.kwargs["client_id"]
        client = Client.objects.get(pk=client_id)
        context["client"] = client
        context["client_id"] = client_id
        context["period"] = period
        return context


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "create_product.html"
    success_url = reverse_lazy("all_clients")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get("client_id")
        context["client_id"] = client_id
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "update_product.html"
    success_url = reverse_lazy("hw5_app:client_products")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get("client_id")
        context["client_id"] = client_id
        return context

    def get_object(self, queryset=None):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, pk=product_id)

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)

