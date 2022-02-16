from django.urls import path
from api.views import ArticleList, ArticleDetail
from api.views import LaunchList, LaunchDetail
from api.views import EventList, EventDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = 'api'
schema_view = get_schema_view(
    openapi.Info(
        title="Space Flight API",
        default_version='v1',
        description="Space Flight Articles API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('launches/', LaunchList.as_view(), name='launch_list'),
    path('launches/<pk>', LaunchDetail.as_view(), name='launch_detail'),
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<pk>', EventDetail.as_view(), name='event_detail'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='api_documentation'),
]
