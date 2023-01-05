from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed

def show_feed(request):
    return HttpResponse("This is Feed Page")

def one_feed(request, feed_id):
    feed = Feed.objects.get(id=feed_id)
    # return HttpResponse(f"Feed Id is {feed_id}")
    return render(request, "feed.html", {"data":feed})

def all_feed(request):
    feeds = Feed.objects.all()
    return render(request, "feeds.html", {"datas":feeds, "title":"전체 피드 데이터"})