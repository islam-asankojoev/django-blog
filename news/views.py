from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from course.serializers import CourseSerializer
from .models import News, Category
from course.models import Course
from .serializers import NewsSerializer
from .tasks import parsing


# Create your views here.
# def index(request):
#     news = News.objects.all()
#     parsing.delay()
class NewsList(ListView):
    model = News
    template_name = 'news/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.all()[::-1]
        context['news'] = News.objects.all()
        # parsing.delay()
        return context

class NewsAll(ListView):
    model = News

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news'] = News.objects.all()
        # parsing.delay()
        return context

def fucking(request):
    context = {
        'asd': 'asd'
    }

    return render(request, 'news/api.html', context)


def newsByCategory(request, title):
    category = Category.objects.get(title=title)
    categories = Category.objects.all()

    news = category.news.all()



    context = {
                'news': news,
                'categories': categories,
                'category': category
               }
    return render(request, 'news/newsByCategory.html', context)

class NewsDetail(DetailView):
    model = News


class CourseDetail(DetailView):
    model = Course





class CourseList(ListView):
    model = Course
    context_object_name = 'course'



class NewsApi(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CourseApi(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer







#     return render(request, 'news/news_detail.html', context={'object': new})
