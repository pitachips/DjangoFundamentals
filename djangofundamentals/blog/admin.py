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
    list_display=['id', 'title', 'status', 'content_size', 'tag_list', 'created_at', 'updated_at']
    actions = ['make_published', 'make_draft']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    # 포스트 내용의 글자 수를 카운트 하는 함수를 만들어서 보여줄 수 있음
    # 인자로는 1)self, 2)Post 모델의 인스턴스
    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    # list_display에는 소괄호 없이 함수의 이름만을 넣는다
    content_size.short_description = '글자수'

    # get_queryset 재정의 없으면 이 함수는 각 post에 대응하는 tag를 가져오기 위해 post갯수만큼 DB에 접근
    def tag_list(self, post):
        return ', '.join(tag.name for tag in post.tag_set.all())

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
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'post_status', 'post_title', 'post_content_len']

    def post_status(self, comment):
        return comment.post.status

    def post_title(self, comment):
        return comment.post.title

    def post_content_len(self, comment):  # 여기는 Comment 모델이 아니라 CommentAdmin 클래스이므로 comment 별도로 인자로 넣어줘야 함
        return len(comment.post.content)

    # list_select_related = ['post'] 
    # select_related 관계에 대해서는 간편한 인터페이스 제공되나 아래와 같이 코딩할 수도 있음
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')





@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
