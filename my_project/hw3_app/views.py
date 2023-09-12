from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView

from hw3_app.models import Order


MAIN_MENU = [
            {'href': 'index', 'name': 'Главная'},
            {'href': 'about', 'name': 'О компании'},
            {'href': 'orders', 'name': 'Заказы'},
            {'href': 'contact', 'name': 'Контакты'},

        ]

class Home(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class Contact(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        return context


class Orders(ListView):
    template_name = 'orders.html'
    model = Order
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menu'] = MAIN_MENU
        context['orders'] = Order.objects.all()
        return context


