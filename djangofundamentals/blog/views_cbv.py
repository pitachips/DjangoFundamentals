from django import forms
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# post_list = ListView.as_view(
#     model=Post,
#     queryset=Post.objects.all().select_related('user').prefetch_related('comment_set', 'tag_set'),
#     # queryset 미지정 시 디폴트는 Post.objects.all()
#     paginate_by=20
#     )

# 위에서 post_list의 인자가 복잡해졌으므로, 상속으로 구현하여 가독성을 증대시키자

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().select_related('user').prefetch_related('comment_set', 'tag_set')
    paginate_by = 20

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)
post_new = CreateView.as_view(model=Post, fields='__all__')
post_edit = UpdateView.as_view(model=Post, fields='__all__')


from django.urls import reverse_lazy

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list')) # success_url 필수임

''' reverse를 사용할 경우 발생하는 에러 메시지
raise ImproperlyConfigured(msg.format(name=self.urlconf_name))
django.core.exceptions.ImproperlyConfigured:
The included URLconf 'djangofundamentals.urls' does not appear to have any patterns in it.
If you see valid patterns in the file then the issue is probably caused by a circular import.
'''
