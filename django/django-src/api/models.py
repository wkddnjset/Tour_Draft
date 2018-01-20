from django.conf import settings
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120,  null=True, blank=True)
    content     = models.TextField(max_length=120, null=True, blank=True)
    timestamp   = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)