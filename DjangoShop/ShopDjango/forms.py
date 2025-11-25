from django import forms
# from .models import 


class CartForm(forms.Form):
    Item = forms.CharField(
        label="Назва продукту",
        widget=forms.TextInput(attrs={"class": "form-control"}))
    Final_Price = forms.CharField(
        label="Фінальна ціна",
        widget=forms.TextInput(attrs={"class": "form-control"}),
)
    
class ItemForm(forms.Form):
    Name = forms.CharField(
        label="Назва продукту",
        widget=forms.TextInput(attrs={"class": "form-control"}))
    Price = forms.CharField(
        label="Ціна продукту",
        widget=forms.TextInput(attrs={"class": "form-control"}),
)