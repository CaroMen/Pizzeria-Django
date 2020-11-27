from django import forms
from .models import Pizza, Topping


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name': ''}
        widgets = {'name': forms.Textarea(attrs={'cols': 80})}
