from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('api/news', NewsApi)
router.register('api/course', CourseApi)
# router.register('api/news/<int:pk>', NewsApi)

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    path('news/<int:pk>', NewsDetail.as_view(), name='singlePost'),
    path('course/<int:pk>', CourseDetail.as_view(), name='singleCourse'),
    path('news', NewsAll.as_view(), name="all_news"),
    path('news/<str:title>', newsByCategory, name='newsByCategory'),
    path('course', CourseList.as_view(), name='courseAll'),
    path('API/', all_api, name='dataAll'),
]

urlpatterns += router.urls

print(urlpatterns)
