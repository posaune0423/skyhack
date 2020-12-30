from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "created_at",
            "country",
            "image1",
            "image2",
            "image3",
            "image4",
            "image5",
            "author",
            "rate"
        )
