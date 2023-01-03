from django.db import models

## Feed (게시글)
## - User
## - Review (댓글)

## - img
## - like
## - content
class Feed(models.Model):
    img = models.ImageField(blank=True, null=True)
    like = models.PositiveIntegerField()
    content = models.TextField(max_length=200)