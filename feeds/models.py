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
    tag = "" # 여행, 독서, 연애 
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # user = models.ForeignKey("users.User", on_delete=models.SET_NULL)

    def __str__(self):
        return self.content