from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed

def show_feed(request):
    return HttpResponse("This is Feed Page")

def one_feed(request, feed_id):
    try:
        feed = Feed.objects.get(id=feed_id)
        return render(request, "feed.html", {"feed":feed})
    except Feed.DoesNotExist:
        return render(request, "feed.html", {"error":False})

def all_feed(request):
    feeds = Feed.objects.all()
    return render(request, "feeds.html", {"datas":feeds, "title":"전체 피드 데이터"})