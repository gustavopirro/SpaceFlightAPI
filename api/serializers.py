from rest_framework import serializers
from api.models import Article
from api.models import Launch
from api.models import Event


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    launches = LaunchSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1

    def create(self, validated_data, *args, **kwargs):
        events = validated_data.pop('events')
        launches = validated_data.pop('launches')

        new_article = Article.objects.get_or_create(
            id=validated_data['id'], defaults=validated_data
        )[0]

        for event in events:
            event_obj = Event.objects.get_or_create(id=event['id'], defaults=event)[0]
            new_article.events.add(event_obj)

        for launch in launches:
            launch_obj = Launch.objects.get_or_create(id=launch['id'], defaults=launch)[0]
            new_article.launches.add(launch_obj)

        return new_article
