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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE) # id=1
    # feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE) # id=1

# Review1 1
#     User1 N
#     User2
#     User3

# User1 1
#     Review1 N
#     Review2
#     Review3
#     Review4
#     Review5

# Feed1 1
#     Review1 N
#     Review2
#     Review3
#     Review4

# Revie1 1
#     Feed1 N
#     Feed2
#     Feed3
