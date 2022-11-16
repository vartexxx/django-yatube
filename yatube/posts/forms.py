from django.forms import ModelForm

from .models import Post


class PostForm(ModelForm):
    class Meta:
        fields = ('text', 'group', 'image')
        model = Post
