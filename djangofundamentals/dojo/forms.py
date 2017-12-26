from django import forms
from .models import Post


# validator 함수는 항상 value 한개를 인자로 받으며, raise forms.ValidationError 를 내포
def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상 입력해주세요')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)  # 사용자에게 보일때 Textarea로 달라 보이게 함
    # models.py 에서 content = models.TextField()로 지정한 것은 DB에게 content가 CharField와 달리 길이제한이 없는 컬럼이라는 것을 알려줌
    # 그러나 forms.py는 DB컬럼타입에 영향을 미치지 않으며, 파이썬은 CharField나 TextField나 동일하게 content를 str으로 세팅함
    # 그러므로 forms.TextField()는 존재하지도 않으며, 결국 CharField()를 사용 

    def save(self, commit=True):    
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post