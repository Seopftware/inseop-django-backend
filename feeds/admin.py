from django.contrib import admin
from .models import Feed


# Register your models here.
@admin.register(Feed)
class FeedsAdmin(admin.ModelAdmin):
    list_display = ("img", "like", "content", "created", "updated")