from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import UserCreateSerializer


User = get_user_model()


class UsersViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    pagination_class = PageNumberPagination
