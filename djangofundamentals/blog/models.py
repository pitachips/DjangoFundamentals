from django.db import models

# Create your models here.

import re
from django.forms import ValidationError
# validation function은 value 하나를 인자로 받으며,
# return 값이 아니라 오류가 있을 경우 raise Error가 필요한 형태
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+.?\d+),\s?([+-]?\d+.?\d+)$', value):  #\s?는 띄어쓰기가 0 또는 1개 있음을 의미
        raise ValidationError('Invalid lnglat')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', help_text='100자 이내로 제목을 적어주세요')  # 길이제한이 있는 문자열
    content = models.TextField(verbose_name="내용")   # 길이제한이 없는 문자열. DB를 위한 구분
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

