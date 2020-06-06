from rest_framework import serializers

from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    created = serializers.SerializerMethodField()
    def get_created(self, comment: Comment):
        return comment.created.timestamp()

    class Meta:
        model = Comment
        fields = ('created', 'user', 'content')
