from django.db import models

from .users import User, DeletedUser


class Post(models.Model):

    created = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.SET(DeletedUser), related_name='posts')

    title = models.CharField(max_length=128)
    content = models.TextField(max_length=4096)

    # <- comments (Comment)++

    likes = models.ManyToManyField(User, related_name='posts_liked')
    visits = models.ManyToManyField(User, related_name='posts_visited')

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('created',)

    def __str__(self): return ' | '.join((self.title, self.author.username, str(self.created.timestamp())))
