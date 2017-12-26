from django.conf.urls import url
from . import views, views_cbv

urlpatterns = [
    url(r'^new/$', views.post_new),

    url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum2),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>[\d]{1,3})/$', views.hello),  # 최소 2자리, 최대4자리의 표현: {2,4}

    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),    
    url(r'^list3/$', views.post_list3),    
    url(r'^excel-down/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),    
    url(r'^cbv/list3/$', views_cbv.post_list3),    
    url(r'^cbv/excel-down/$', views_cbv.excel_download),
]
