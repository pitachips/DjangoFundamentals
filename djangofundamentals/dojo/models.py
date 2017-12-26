from django.db import models
from django.urls import reverse
# Create your models here.


from django import forms

# validator 함수는 항상 value 한개를 인자로 받으며, raise forms.ValidationError 를 내포
# validator는 forms.py가 아니라 models.py 에서 작성해야 옳음. Fat Model
def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    user_agent = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('dojo:post_detail', args=[self.id])


from django.core.validators import MinLengthValidator

# Chapter 23
class GameUser(models.Model):
    server = models.CharField(max_length=1, choices=(
        ('A', 'A서버'),
        ('B', 'B서버'),
        ('C', 'C서버'),)
    )
    username = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    # MinLengthValidator(3)을 통해 username이 3글자 "이상"일 것을 검사

    class Meta:
        unique_together = [
            ('server', 'username'),  # str이어야함
        ]
        # unique_together를 통해 두가지 필드 조합의 유일성 검사
