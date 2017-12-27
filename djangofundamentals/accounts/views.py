from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm


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