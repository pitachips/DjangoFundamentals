from django.db import models
from django.conf import settings
# Create your models here.

import re
from django.forms import ValidationError
# validation function은 value 하나를 인자로 받으며,
# return 값이 아니라 오류가 있을 경우 raise Error가 필요한 형태
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+.?\d+),\s?([+-]?\d+.?\d+)$', value):  #\s?는 띄어쓰기가 0 또는 1개 있음을 의미
        raise ValidationError('Invalid lnglat')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published'),
        ('w', 'withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    title = models.CharField(max_length=100, verbose_name='제목', help_text='100자 이내로 제목을 적어주세요')  # 길이제한이 있는 문자열
    content = models.TextField(verbose_name="내용")   # 길이제한이 없는 문자열. DB를 위한 구분
    tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)   # Tag를 문자열로 감싸서 넣어줄 것. 그래야 undefined 에러 피할 수 있음
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    # __str__과 같은 함수는 DB의 칼럼에 반영되지 않으므로 migration 불필요함
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)   # 'Post'로 넣어줘도 좋음.
    # DB 상에는 post_id 를 이름으로 하는 컬럼이 생성됨!!
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name