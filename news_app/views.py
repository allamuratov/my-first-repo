from django.shortcuts import render, get_object_or_404
from .models import News, Category


# Create your views here.
def news_list(request):
    news_list = News.objects.filter(status=News.Status.Publish)
    context = {
        'news_list':news_list
    }

    return render(request,'news_list.html', context=context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Publish)
    context = {
        "news": news
    }
    return render(request, 'news_detail.html', context)


def homePageView(request):
    news = News.objects.filter(status=News.Status.Publish)
    category = Category.objects.all()
    context = {
        'news': news,
        'category': category
    }

    return render(request, 'index.html', context)

def contactPageView(request):
    context = {

    }

    return render(request, 'contact.html', context)