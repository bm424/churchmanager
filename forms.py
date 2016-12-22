from django import forms

from .models import Church


class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = '__all__'
        widgets = {
            'classification': forms.RadioSelect,
        }
