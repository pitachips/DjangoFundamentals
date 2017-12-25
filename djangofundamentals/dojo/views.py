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
