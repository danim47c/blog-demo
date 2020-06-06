from django.db import models

from .users import User, DeletedUser
from .posts import Post


class Comment(models.Model):

    created = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.SET(DeletedUser), related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField(max_length=512)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('created',)

    def __str__(self): return ' - '.join((self.post, self.author, self.created))
