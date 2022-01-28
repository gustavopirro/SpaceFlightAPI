from django.urls import path
from api.views import ArticleList, ArticleDetail
from api.views import LaunchList, LaunchDetail
from api.views import EventList, EventDetail


urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('launches/', LaunchList.as_view(), name='launch_list'),
    path('launches/<int:pk>', LaunchDetail.as_view(), name='launch_detail'),
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<int:pk>', EventDetail.as_view(), name='event_detail'),
]
