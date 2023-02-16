from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    ユーザー
    """
    class Meta:
        model = User
        fields = '__all__'
