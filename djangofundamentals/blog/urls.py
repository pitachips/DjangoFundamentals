from django.conf.urls import url
from . import views, views_cbv

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^new/$', views.post_new, name='post_new'),
    # url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^new/$', views_cbv.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),    
]
