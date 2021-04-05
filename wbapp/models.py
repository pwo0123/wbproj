from django.db import models


class CFS(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=40)
    is_active = models.BooleanField(default=False)

