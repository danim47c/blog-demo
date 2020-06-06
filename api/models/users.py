from django.contrib.auth.hashers import check_password, make_password
from django.db import models

from binascii import hexlify
from os import urandom


class User(models.Model):

    joined = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=128, unique=True)

    password = models.CharField(max_length=78)
    password_hash = models.CharField(max_length=78, null=True, editable=False)

    token = models.CharField(max_length=48, null=True, editable=False)

    # <- posts (Post)++
    # <- posts_liked (Post)++
    # <- posts_visited (Post)++

    # <- comments (Comment)++

    def save(self, *args, **kwargs):
        if not self.password_hash or not check_password(self.password, self.password_hash):
            self.password = make_password(self.password)
            self.password_hash = make_password(self.password)

        if not self.token: self.generate_token()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ('joined',)

    def __str__(self): return self.username

    def generate_token(self):
        self.token = hexlify(urandom(24)).decode()

    def check_password(self, password: str):
        return check_password(password, self.password)


class DeletedUser(object):

    id = -1

    username = 'Deleted User'
