from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    """
    ユーザー登録フォーム
    """
    class Meta(UserCreationForm.Meta):
        model   = User
        fields  = ("username", "full_name")