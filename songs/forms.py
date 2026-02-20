import re
from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    duration_display = forms.CharField(
        label='Duration (MM:SS)',
        help_text='Enter duration in minutes:seconds format (e.g., 3:17)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., 3:17'
        })
    )

    class Meta:
        model = Song
        fields = ['title', 'duration_display', 'release_year', 'band', 'lyrics_preview']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Enter Sandman'
            }),
            'release_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': 2026,
                'placeholder': 'e.g., 1991'
            }),
            'band': forms.Select(attrs={
                'class': 'form-control'
            }),
            'lyrics_preview': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Optional: Enter a preview of the lyrics...'
            }),
        }
        labels = {
            'title': 'Song Title',
            'release_year': 'Release Year',
            'band': 'Band',
            'lyrics_preview': 'Lyrics Preview',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            minutes = self.instance.duration // 60
            seconds = self.instance.duration % 60
            self.fields['duration_display'].initial = f"{minutes}:{seconds:02d}"

        if self.instance and self.instance.pk:
            self.fields['band'].disabled = True
            self.fields['band'].help_text = "Band cannot be changed after creation"

    def clean_duration_display(self):
        duration_str = self.cleaned_data.get('duration_display')

        pattern = r'^(\d+):(\d{1,2})$'
        match = re.match(pattern, duration_str)

        if not match:
            raise forms.ValidationError('Please use MM:SS format (e.g., 3:17 or 12:05)')

        minutes = int(match.group(1))
        seconds = int(match.group(2))

        if seconds >= 60:
            raise forms.ValidationError('Seconds must be less than 60')

        if minutes > 60:
            raise forms.ValidationError('Minutes cannot exceed 60')

        total_seconds = minutes * 60 + seconds

        return total_seconds

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError('Song title must be at least 2 characters long.')
        return title

    def clean_release_year(self):
        year = self.cleaned_data.get('release_year')
        if year:
            if year < 1900 or year > 2100:
                raise forms.ValidationError('Release year must be between 1900 and 2100')
        return year

    def save(self, commit=True):
        self.instance.duration = self.cleaned_data['duration_display']
        return super().save(commit)