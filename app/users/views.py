from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


class UserRegistrationView(CreateAPIView):
    """
        API для регистрации пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
