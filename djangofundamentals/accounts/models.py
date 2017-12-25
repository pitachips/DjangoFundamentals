from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

# user 를 받아오는 방법

# 1. user = models.OneToOneField('auth.User')

# 2. 좋지 못한 방법
# from django.contrib.auth.models import User
# user = models.OneToOneField(User)

# 3. user = models.ForeignKey()