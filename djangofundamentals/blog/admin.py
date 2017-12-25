from django.contrib import admin
from .models import Post
# Register your models here.


# 가장 기본적인 admin 이용
admin.site.register(Post)
admin.site.unregister(Post)

# 기본 admim + 커스터마이징 (1. 상속)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at']
admin.site.register(Post, PostAdmin)
admin.site.unregister(Post)   # unregister는 모델을 통째로 인자로 넣어서 함.

# 기본 admin + 커스터마이징 (2. 장식자)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at']
