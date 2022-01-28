from django.urls import path
from api.views import hello_world


urlpatterns = [
    path('helloworld/', hello_world, name='hello_world')
]
