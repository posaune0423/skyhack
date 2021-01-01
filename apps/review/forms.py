from datetime import date
from django import forms


from .models import Review


class ReviewForm(forms.ModelForm):
    created_at = forms.DateField(label='Date', initial=date.today())

    class Meta:
        model = Review

        fields = (
            'title',
            'body',
            'created_at',
            'airport',
            'rate'
        )
        labels = {
            'title': 'Review Title',
            'body': 'Review Content',
        }
