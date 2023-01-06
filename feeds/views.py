from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Feed
from .serializers import FeedsSerializer

# Objects => JSON
class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all() # objects
        print("feeds")
        print(feeds)

        # objects => JSON: Serializer가 해준다.
        serializer = FeedsSerializer(feeds, many=True)
        print("serializer")
        print(serializer)

        return Response(serializer.data)