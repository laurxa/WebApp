from django import forms

from .models import Citation


class CitationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs = {
            'class': 'materialize-textarea',
        }

    class Meta:
        model = Citation
        fields = ['title', 'content']
