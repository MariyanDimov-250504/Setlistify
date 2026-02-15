from django import forms
from .models import Concert, SetlistEntry
from songs.models import Song

class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ['band', 'venue', 'city', 'date', 'tour_name', 'notes']
        widgets = {
            'band': forms.Select(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Madison Square Garden'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., New York, NY'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'tour_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., World Tour 2024 (optional)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any special notes about this concert...'
            }),
        }
        labels = {
            'band': 'Band',
            'venue': 'Venue',
            'city': 'City',
            'date': 'Concert Date',
            'tour_name': 'Tour Name',
            'notes': 'Additional Notes',
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        return date


class SetlistEntryForm(forms.ModelForm):
    class Meta:
        model = SetlistEntry
        fields = ['song', 'order', 'encore', 'notes']
        widgets = {
            'song': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Song order (1, 2, 3...)'
            }),
            'encore': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional notes about this performance'
            }),
        }
        labels = {
            'song': 'Song',
            'order': 'Order',
            'encore': 'Encore Performance',
            'notes': 'Notes',
        }

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if order < 1:
            raise forms.ValidationError('Order must be at least 1.')
        return order
