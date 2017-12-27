from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Chapter 3
def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))


def mysum2(request, numbers):
    # result = sum(map(int), numbers.split('/'))) 를 수행하면 빈문자열에 대한 int()에서 에러발생
    result = sum(map(lambda n: int(n or 0), numbers.split('/')))
    return HttpResponse(result)


def hello(request, name, age):
    result = '안녕하세요. {}님, {}살 이시네요.'.format(name, age)
    return HttpResponse(result)


# Chapter 4
def post_list1(request):
    'FBV: 직접 문자열로 HTML 형식 응답하기'
    return HttpResponse('''
        <h1>Django Fundamentals</h1>
        <p>{chapter}</p>
        <p>뷰에 대한 오버뷰</p>
        '''.format(chapter='Ch.4'))


from django.shortcuts import render

def post_list2(request):
    'FBV: 템플릿을 통해 HTML형식 응답하기'
    name = '공유'
    response = render(request, 'dojo/post_list2.html', {'name':name})
    return response


from django.http import JsonResponse

def post_list3(request):
    'FBV: JSON 형식 응답하기'
    return JsonResponse({
        'message':'Django Fundamentals',
        'items': ['파이썬', '장고', 'celery', 'AWS'],},
        json_dumps_params={'ensure_ascii': False})



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'dojo/post_detail.html', {
        'post': post,
    })


import os
# from djangofundamentals import settings
from django.conf import settings

def excel_download(request):
    'FBV: 엑셀 다운로드 응답하기'
    # path는 항상 하드코딩보다 상대적 경로가 좋음
    # filepath = r'C:\Users\Tirius\py-proj\DjangoFundamentals\djangofundamentals\dojo\others\Book1.xls'
    filepath = os.path.join(settings.BASE_DIR, 'dojo/others/Book1.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        # content_type 미지정 시 디폴트는 'text/html'
        # 'application/vnd.ms-excel'는 파일을 xls 형식으로 다운로드함
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 헤더설정은 항상 도움이 됨. 이걸 설정해야 다운로드 파일이름이 filename으로 받아짐!
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

# Chapter 21
def post_new(request):
    # if request.method == 'GET': 으로 시작할 수도 있으나, 
    # POST인 경우에 로직이 많으므로 POST를 앞에 놓고 GET인 경우를 else에 서술하는 것이 장고가 선호하는 스타일
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # 유저가 뭔가를 입력or업로드 한 것들을 form에 넣어줘야 함. POST와 FILES 순서 바뀌면 안됨
        if form.is_valid():  # 이 시점에서 form과 관련된 모든 validators가 호출됨
            post = form.save(commit=False) # 각종 save방법에 대해 Chapter21.ipynb 참고
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)  #namespace:name 사용가능
        else: # validation 실패 시, form.errors와 form.각필드.errors에 오류정보 저장 (html <ul> <li> 형태)
            print(form.errors)
    else:
        form = PostForm()  # form을 GET한다는 것은 그냥 쌩 첫 폼을 원한다는 뜻임

    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


from django.shortcuts import get_object_or_404

# Chapter 22
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)  # 이 부분과 instance=post 추가가 필요

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # 유저가 뭔가를 입력or업로드 한 것들을 form에 넣어줘야 함. POST와 FILES 순서 바뀌면 안됨
        if form.is_valid():  # 이 시점에서 form과 관련된 모든 validators가 호출됨
            post = form.save(commit=False) # 각종 save방법에 대해 Chapter21.ipynb 참고
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)  #namespace:name 사용가능
        else: # validation 실패 시, form.errors와 form.각필드.errors에 오류정보 저장 (html <ul> <li> 형태)
            print(form.errors)
    else:
        form = PostForm(instance=post)  # form을 GET한다는 것은 그냥 쌩 첫 폼을 원한다는 뜻임

    return render(request, 'dojo/post_form.html', {
        'form': form,
    })
