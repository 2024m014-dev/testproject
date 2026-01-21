from django.db import models
from django.contrib.auth.models import User


class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


class GachaResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.result_text
