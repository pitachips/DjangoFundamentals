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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('dojo:post_detail', args=[self.id])

