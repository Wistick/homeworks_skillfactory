from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'time_created': ['gt'],
            'title': ['icontains'],
            'post_author': ['exact'],
        }
