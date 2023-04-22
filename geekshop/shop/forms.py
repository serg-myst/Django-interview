from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit_measure'].empty_label = "Выберите единицу измерения"

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'full_name', 'price', 'description', 'unit_measure']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_name',
                    'placeholder': 'Name',
                    "autofocus": True,
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_full_name',
                    'placeholder': 'Full name',
                    "autofocus": True,
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'id_price',
                    'placeholder': 'Price',
                    "autofocus": True,
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'id_description',
                    'placeholder': 'Description',
                    "autofocus": True,
                }
            ),
            'unit_measure': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'unit_measure',
                }
            ),
        }