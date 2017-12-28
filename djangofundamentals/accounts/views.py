from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # 회원가입 이후 로그인 페이지로 이동
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form})    


from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# login_required의 역할
# 1) 비 로그인 상태라면 LOGIN_URL 로 데려감
# 2) ?next={{ request.path }} 를 자동으로 붙여서 로그인 시 그 url로 갈 수 있게 함


from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
# get_providers() 함수는 settings/INSATALLED_APPS에 활성화된 provider 목록을 리턴함

def login(request):
    providers =[]
    for provider in get_providers():
        try:  # 실제 provider별 id/pw가 등록되어있는지 시도
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
            # social_app 속성은 본래 provider에는 없는 속성임
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers}
    )