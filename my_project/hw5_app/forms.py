from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
            "quantity",
            "photo",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": ". . ."}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": ". . ."}
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": ". . ."}
            ),
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": ". . ."}
            ),
            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control-file btn btn-outline-secondary btn-sm"
                }
            ),
        }
        labels = {
            "name": "Название",
            "description": "Описание",
            "category": "Категория",
            "price": "Стоимость",
            "quantity": "Количество единиц",
            "photo": "Фото товара",
        }