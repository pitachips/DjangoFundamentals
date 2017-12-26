from django import forms
from .models import Post



# Chapter 22
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content']

    ''' ModelForm에는 아래와 같은 내용이 작성되어 있음. 그래서 반자동으로 form.save()에 의해 DB에 인스턴스 생성&저장됨
    def save(self, commit=True):
        self.instance = Post(**cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    '''


'''
# Chapter 21
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
'''


from .models import GameUser

# Chapter 23
class GameUserForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['server', 'username']

    def clean_username(self):   # 함수명과 인자는 거의 고정적. clean_필드명(self)
        return self.cleaned_data.get('username', '').strip() 