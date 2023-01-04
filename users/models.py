from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
## User (유저)
## - id(prmary key, unique) // django에서 자동으로 생성됨. 중복될 수 없다.
## - pw // django 자동으로 생성됨.
## - email
## - nickname
## - phone
## - gender
## - profileImg
## - Feed (게시글)
## - Follow (팔로우)
## - profileIntroduce
## - is_business (Boolean)

# class User(models.Model):
class User(AbstractUser):
    nickname = models.CharField(max_length=30, default="")
    phone = models.PositiveIntegerField(default=0) # 01011111111 # 양의 정수형 숫자
    is_business = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, default="")
    profileIntroduce = models.TextField(max_length=200, default="")
    sns = models.CharField(max_length=10, default="")
    # pass