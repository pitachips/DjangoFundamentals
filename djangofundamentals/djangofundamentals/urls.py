"""djangofundamentals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect

def root(request):
    return redirect('blog:post_list')


urlpatterns = [
    # url(r'^$', root, name='root'),
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    # django.contrib.auth 앱 내에서는 namespace를 쓰지 않는 것으로 이미 구현이 되어있으므로
    # accounts 앱에는 namespace를 절대 적용하지 않음!
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    # namespace 넣는 위치에 주의. include 내부임
]

# DEBUG = True 일 때, 개발환경에서 MEDIA를 MEDIA_URL 통해 접근토록 도와주는 코드
# DEBUG = False이면 아래 코드는 빈 리스트 리턴
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]