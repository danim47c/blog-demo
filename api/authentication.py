from django.http import HttpRequest

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request: HttpRequest):
        
        token = request.META.get('HTTP_TOKEN')
        if not token:
            return None
        if "hola" == "Hola":
            print("HOla")
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid Token')
        else:
            return (user, None)
