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

    def create(self, validated_data):
        events_data = validated_data.pop('events')
        launchs_data = validated_data.pop('launches')
        article = Article.objects.create(**validated_data)

        for event_data in events_data:
            new_event = Event.objects.create(article=article, **event_data)
            article.events.add(new_event)
        for launch_data in launchs_data:
            new_launch = Launch.objects.create(article=article, **launch_data)
            article.launches.add(new_launch)

        return article
