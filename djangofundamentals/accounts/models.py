from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # DB에선 user_id 라는 컬럼이 생성됨
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

# user 를 받아오는 잘못된 방법들(Ch.11)과 달리 settings.AUTH_USER_MODEL을 이용하면 커스터마이징이 가능해짐
