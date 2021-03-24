from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['post_author', 'choice_field', 'post_category', 'title', 'text']
