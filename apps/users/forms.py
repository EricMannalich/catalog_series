from django.contrib.auth.forms import UserCreationForm
# the user model was customized it should be invoked
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from apps.users.models import User as CustomUser


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = CustomUser

class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # the user model was customized it should be invoked
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email",)