from django.db import models
from django.conf import settings

# Create your models here.


class Blogs(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
