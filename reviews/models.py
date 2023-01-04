from django.db import models
from common.models import CommonModel

## Review (댓글)
## - User
## - content
## - like
## - reply

class Review(CommonModel):
    content = models.CharField(max_length=120)
    like = models.PositiveIntegerField()
    reply = models.BooleanField(default=False)