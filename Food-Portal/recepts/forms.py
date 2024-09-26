from django import forms
from django.core.exceptions import ValidationError

from .models import Recept


class ProductForm(forms.ModelForm):

    class Meta:
        model = Recept
        fields = ['title', 'text', 'ccal']

    def clean(self, form):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data