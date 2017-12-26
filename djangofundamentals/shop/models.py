from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop_post_set')
    # related_name='+' 지정은 이 컬럼에 대해 user.post_set.all()과 같은 reverse access를 포기하겠다는 뜻임
    # 그러나 Post.objects.filter(user=user)와 같은 접근은 사용
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
