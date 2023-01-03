from django.db import models

## Review (댓글)
## - User
## - content
## - like
## - reply

class Review(models.Model):
    content = models.CharField(max_length=120)
    like = models.PositiveIntegerField()
    reply = models.BooleanField(default=False)