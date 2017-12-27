from django import forms
from .models import Post
from djangofundamentals.widgets.naver_map_point_widget import NaverMapPointWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'content', 'tag_set', 'status', 'lnglat']
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width':600, 'height':300}),
        }
