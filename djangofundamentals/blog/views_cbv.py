from django import forms
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

post_list = ListView.as_view(model=Post, paginate_by=20)
post_detail = DetailView.as_view(model=Post)
post_new = CreateView.as_view(model=Post, fields='__all__')
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url='/blog/') # success_url 필수임
