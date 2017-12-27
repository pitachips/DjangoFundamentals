from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )
        # UserCreationForm에서 fields를 튜플형태로 정의하고 있어서 마찬가지로 튜플로 add 해줌
        # email은 class AbstractUser에서 email 필드가 있기때문에 fields에 넣는것만으로 곧장 사용가능
        