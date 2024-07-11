from django.core.exceptions import ValidationError
from catalog.models import Products, ProductVersions

from django.forms import ModelForm, BooleanField


class StyleFormMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductsForm(StyleFormMixin, ModelForm):
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


class ProductVersion(StyleFormMixin, ModelForm):
    class Meta:
        model = ProductVersions
        fields = '__all__'
