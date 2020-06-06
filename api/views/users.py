from django.db.utils import IntegrityError

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models import User

from ..serializers import UserSerializer

from ..permissions import IsAuthenticated


class UserViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def login(self, request: Request):
        try:
            user = User.objects.get(username=request.data['username'])

            if not user.check_password(request.data['password']):
                return Response(
                    {
                        'detail': 'Incorrect password.'
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

        except User.DoesNotExist:
            return Response(
                {
                    'detail': 'User not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except KeyError:
            return Response(
                {
                    'detail': '"username" and "password" fields are required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        else:

            user.generate_token()

            user.save()

            return Response(
                {
                    'id': user.id,
                    'token': user.token
                }
            )

    @action(detail=False, methods=['post'])
    def register(self, request: Request):
        try:
            user = User.objects.create(
                username=request.data['username'],
                password=request.data['password']
            )

        except IntegrityError:
            return Response(
                {
                    'detail': 'Username taken.'
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        except KeyError:
            return Response(
                {
                    'detail': '"username" and "password" fields are required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        else:
            return Response({"token": user.token})

    @action(detail=True, methods=['post'])
    def change_password(self, request: Request, pk: int):
        try:
            user = self.get_object()

            if not user == request.user:
                raise PermissionDenied()

            if not user.check_password(request.data['old_password']):
                return Response(
                    {
                        'detail': 'Incorrect password.'
                    }
                )

            else:
                user.password = request.data['new_password']

        except KeyError:
            return Response(
                {
                    'detail': '"old_password" and "new_password" fields are required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        else:
            return Response(
                {
                    'detail': 'Password changed successfully.'
                }
            )

    @action(detail=False, methods=['post'])
    def check_token(self, request: Request):
        user = request.user

        user.generate_token()
        user.save()

        return Response(
            {
                'id': user.id,
                'token': user.token
            }
        )

    def get_permissions(self):
        self.permission_classes = []

        if self.action in ['change_password', 'check_token']:
            self.permission_classes.append(IsAuthenticated)

        return super().get_permissions()
