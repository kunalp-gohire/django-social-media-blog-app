from django.db import models
from django.conf import settings
from django.urls import reverse
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',
                       kwargs={
                           'username': self.user.username,
                           'pk': self.pk
                       })

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    # text_html = models.TextField(editable=False,null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('posts:single',
                       kwargs={
                           'username': self.user.username,
                           'pk': self.pk
                       })

    class Meta:
        ordering = ['-created_at']



