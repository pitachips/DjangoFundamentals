from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.


# 가장 기본적인 admin 이용
admin.site.register(Post)
admin.site.unregister(Post)

# 기본 admim + 커스터마이징 (1. 상속)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at']
admin.site.register(Post, PostAdmin)
admin.site.unregister(Post)   # unregister는 모델을 통째로 인자로 넣어서 함.


from django.utils.html import mark_safe

# 기본 admin + 커스터마이징 (2. 장식자) 사용 추천
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'status', 'content_size', 'created_at', 'updated_at']
    actions = ['make_published', 'make_draft']

    # 포스트 내용의 글자 수를 카운트 하는 함수를 만들어서 보여줄 수 있음
    # 인자로는 1)self, 2)Post 모델의 인스턴스
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    # list_display에는 소괄호 없이 함수의 이름만을 넣는다
    content_size.short_description = '글자수'

    # bulk action을 만들기 위한 함수는 항상 인자로 self, request, queryset을 받음 
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')   #QuerySet.update 함수를 사용하여 성능제고
        self.message_user(request, '{} posts successfully updated as published'.format(updated_count)) #django의 message framework 활용
    make_published.short_description = 'Make selected posts as published'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')   #Queryset.update 함수를 사용하여 성능제고
        self.message_user(request, '{} posts successfully updated as draft'.format(updated_count)) #django의 message framework 활용
    make_draft.short_description = 'Make selected posts as draft'


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
