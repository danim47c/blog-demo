from rest_framework import serializers

from ..models import User, Post

from .post import PostSerializer

class UserPostSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created', 'title', 'content', 'comments', 'likes', 'visits')

class UserSerializer(serializers.ModelSerializer):

    joined = serializers.SerializerMethodField()
    def get_joined(self, user: User):
        return user.joined.timestamp()


    posts = UserPostSerializer(many=True, read_only=True)

    posts_liked = serializers.SerializerMethodField()
    def get_posts_liked(self, user: User):
        return user.posts_liked.count()

    posts_visited = serializers.SerializerMethodField()
    def get_posts_visited(self, user: User):
        return user.posts_visited.count()

    comments = serializers.SerializerMethodField()
    def get_comments(self, user: User):
        return user.comments.count()

    class Meta:
        model = User
        fields = ('id', 'joined', 'username', 'posts', 'posts_liked', 'posts_visited', 'comments')
