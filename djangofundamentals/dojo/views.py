from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))


def mysum2(request, numbers):
    # result = sum(map(int), numbers.split('/'))) 를 수행하면 빈문자열에 대한 int()에서 에러발생
    result = sum(map(lambda n: int(n or 0), numbers.split('/')))
    return HttpResponse(result)


def hello(request, name, age):
    result = '안녕하세요. {}님, {}살 이시네요.'.format(name, age)
    return HttpResponse(result)