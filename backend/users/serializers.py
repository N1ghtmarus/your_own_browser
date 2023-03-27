from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя"""
    class Meta:
        model = User
        fields = ('username',) + tuple(User.REQUIRED_FIELDS) + (
            'password',
        )
