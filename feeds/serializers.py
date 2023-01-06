from rest_framework.serializers import ModelSerializer
from .models import Feed

class FeedsSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"