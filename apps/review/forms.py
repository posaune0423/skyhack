from django import forms


from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = (
            'title',
            'body',
            'airport',
            'rate'
        )
        labels = {
            'title': 'Review Title',
            'body': 'Review Content',
        }
