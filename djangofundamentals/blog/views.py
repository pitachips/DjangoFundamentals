from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    qs = Post.objects.all().select_related('user').prefetch_related('comment_set', 'tag_set')
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list':qs,
        'q':q,
    })

from django.http import Http404
from django.shortcuts import get_object_or_404

def post_detail(request, id):
    # post = Post.objects.get(id=id)  
    # 이 경우 게시물 미존재 시 http 500 코드를 응답하는 문제

    # try:
    #     post = Post.objects.get(id=id)
    # except (Post.DoesNotExist, Post.MultipleObjectsReturned):
    #     raise Http404
    # 이렇게 매번 try 구문 쓰는 번거로움을 피하기 위해 get_object_or_404 사용

    post = get_object_or_404(Post, id=id)  # 추천. 게시물 미존재 시 404 코드로 응답

    return render(request, 'blog/post_detail.html', {
        'post':post,
    })


from .forms import PostForm
from django.shortcuts import redirect

from django.contrib import messages

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # Message Framework를 이용하는 방법1(전통)
            # messages.add_message(request, messages.SUCCESS, '새 글이 등록되었습니다!')
            # Message Framework를 이용하는 방법2(shortcut)
            messages.success(request, '새 글이 등록되었습니다!!')
            # message는 redirect 이전에 보내져야 함!
            return redirect(post)    # success_url 아니면 get_absolute_url 경로로 순차적으로 감
    else:
        form = PostForm()
  
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # messages.error(request, '에러에러')
            messages.success(request, '성공적으로 수정되었습니다')
            return redirect(post)    # success_url 아니면 get_absolute_url 경로로 순차적으로 감
    else:
        form = PostForm(instance=post)
  
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


from .models import Comment

def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html', {'comment_list': comment_list})



