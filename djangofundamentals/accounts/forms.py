from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )
        # UserCreationForm에서 fields를 튜플형태로 정의하고 있어서 마찬가지로 튜플로 add 해줌
        # email은 class AbstractUser에서 email 필드가 있기때문에 fields에 넣는것만으로 곧장 사용가능

    def save(self):
        user = super().save()   # UserCreationForm은 model로 User를 두고있으므로 email 값도 여기서 저장됨
        profile = Profile.objects.create(
            user=user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address']
        )
        return user