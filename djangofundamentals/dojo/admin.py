from django.contrib import admin
from .models import Post, GameUser
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
    pass