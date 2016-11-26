from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    titel = models.CharField(max_length=200)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now)
    publish_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_data = timezone.now()
        self.save()

    def __str__(self):
        return self.titel
