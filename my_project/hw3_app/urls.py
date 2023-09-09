from django.urls import path
from . import views
from .views import Home, About, Contact, Orders

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('index', Home.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('orders/', Orders.as_view(), name='orders'),
]
