from rest_framework import serializers

from ..models import Post, User

from .comment import CommentSerializer

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    author = PostUserSerializer(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)

    created = serializers.SerializerMethodField()
    def get_created(self, post: Post):
        return post.created.timestamp()

    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    visits = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'created', 'author', 'title', 'content', 'comments', 'likes', 'visits')
