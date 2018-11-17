from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import HouseModel, Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'description', 'property_id', 'price', 
            'address', 'city', 'state', 'photo'
        )

class SearchForm(forms.Form):
    error_css_class = 'error'

    s = forms.CharField(
        required=False,
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': _('Search by house name or house city')}),
    )

    def clean_s(self):
        s = self.cleaned_data['s'].strip()
        if s and len(s) < 2:
            raise forms.ValidationError(_("The search text must be at least 2 characters"))
        return s


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()