from django import forms
from .models import Band

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'formed_year', 'genre', 'bio', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Metallica, The Beatles'
            }),
            'formed_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': 2026
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Rock, Metal, Pop'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell us about the band...'
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/band-photo.jpg'
            }),
        }
        labels = {
            'name': 'Band Name',
            'formed_year': 'Year Formed',
            'genre': 'Genre',
            'bio': 'Biography',
            'image_url': 'Band Photo URL',
        }
        help_texts = {
            'formed_year': 'Enter the year the band was formed (1900-2026)',
            'image_url': 'Optional: Provide a URL to a band photo',
        }

    def clean_formed_year(self):
        year = self.cleaned_data.get('formed_year')
        if year < 1900 or year > 2026:
            raise forms.ValidationError('Year must be between 1900 and 2026')
        return year

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError('Band name must be at least 2 characters long')
        return name
