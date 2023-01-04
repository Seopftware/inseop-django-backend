from django.db import models
from common.models import CommonModel

## Feed (게시글)
## - User
## - Review (댓글)

## - img
## - like
## - content
class Feed(CommonModel):
    img = models.ImageField(blank=True, null=True)
    like = models.PositiveIntegerField()
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.content