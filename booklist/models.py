from django.contrib.auth.models import User
from django.db import models


class BookModel(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    title = models.CharField('タイトル', max_length=255)
    author = models.CharField('著者', max_length=255)
    summary = models.TextField('あらすじ', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title