from django.core.exceptions import ValidationError
from catalog.models import Products
from django.forms import ModelForm


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        exclude = ("view_counter",)

    def clean_name(self):
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data["name"]
        for word in words:
            if word in cleaned_data:
                raise ValidationError(f'Поле не должно содержать слово {word}')
        return cleaned_data
