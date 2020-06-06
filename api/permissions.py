from django.contrib.auth.models import AnonymousUser

from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import User, Post


class IsAuthenticated(BasePermission):
  def has_permission(self, request, view):
    return not isinstance(request.user, AnonymousUser)

class UserPostOwn(BasePermission):
  def has_object_permission(self, request, view, post: Post):
    return post.author == request.user if not isinstance(request.user, AnonymousUser) else False
