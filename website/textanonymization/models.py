from django.db import models
from django.contrib.auth.models import User


class TextRecords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    redacted_text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


