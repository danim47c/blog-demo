from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models import Post

from ..serializers import PostSerializer


from ..permissions import IsAuthenticated, UserPostOwn


class PostViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request: Request, pk: int):

        if IsAuthenticated():
            post = self.get_object()

            if not request.user == post.author and not request.user in post.visits.all():
                post.visits.add(request.user)

        return super().retrieve(request, pk=pk)

    def create(self, request: Request):

        try:

            post = Post.objects.create(
                author=request.user,
                title=request.data['title'],
                content=request.data['content']
            )

        except KeyError:
            return Response(
                {
                    'detail': '"title" and "content" fields are required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        else:
            return Response(
                PostSerializer(instance=post).data
            )

    def update(self, request: Request, pk: int, partial: bool = False):
        try:
            post = self.get_object()
            post.content = request.data['content']

        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except KeyError:
            return Response(
                {
                    'detail': '"content" field is required'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        else:
            post.save()

            return Response(
                PostSerializer(instance=post).data
            )

    @action(detail=True, methods=['post'])
    def like(self, request: Request, pk: int):
        user = request.user
        post = self.get_object()

        if not user in post.likes.all():
            post.likes.add(user)
        else:
            post.likes.remove(user)

        return Response(
            {
                'detail': 'Post likes updated successfully'
            }
        )

    def get_permissions(self):
        self.permission_classes = []

        if self.action in ['create', 'update', 'partial_update', 'destroy', 'like']:
            self.permission_classes.append(IsAuthenticated)

        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes.append(UserPostOwn)

        return super().get_permissions()
