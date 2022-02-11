from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models import Article
from api.models import Launch
from api.models import Event
from api.serializers import ArticleSerializer
from api.serializers import LaunchSerializer
from api.serializers import EventSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        obj_data = request.data
        events = obj_data.pop('events')
        launches = obj_data.pop('launches')

        new_article, created = Article.objects.get_or_create(**obj_data)

        if created is False:
            return Response(
                {'message': 'Invalid Request', 'status': status.HTTP_400_BAD_REQUEST},
                status.HTTP_400_BAD_REQUEST)

        for event in events:
            event_obj = Event.objects.get_or_create(id=event['id'], defaults=event)[0]
            new_article.events.add(event_obj)

        for launch in launches:
            launch_obj = Launch.objects.get_or_create(id=launch['id'], defaults=launch)[0]
            new_article.launches.add(launch_obj)

        serializer = ArticleSerializer(new_article)
        headers = self.get_success_headers(serializer)
        return Response([serializer.data], status=status.HTTP_201_CREATED, headers=headers)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def put(self, request, pk, *args, **kwargs):
        obj_data = request.data
        events = obj_data.pop('events')
        launches = obj_data.pop('launches')
        article = get_object_or_404(Article, id=pk)
        Article.objects.filter(id=pk).update(**obj_data)

        for event in events:
            event_obj = Event.objects.get_or_create(id=event['id'], defaults=event)[0]
            event_obj.provider = event['provider']
            event_obj.save()
            article.events.add(event_obj)

        for launch in launches:
            launch_obj = Launch.objects.get_or_create(id=launch['id'], defaults=launch)[0]
            launch_obj.provider = launch['provider']
            launch_obj.save()
            article.launches.add(launch_obj)

        serializer = ArticleSerializer(article)
        return Response([serializer.data], status=status.HTTP_202_ACCEPTED)


class LaunchList(generics.ListCreateAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer
    permission_classes = [IsAuthenticated]


class LaunchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer
    permission_classes = [IsAuthenticated]


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
