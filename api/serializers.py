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

        article = Article()
        for k, v in validated_data.items():
            setattr(article, k, v)
        article.save()

        for event_data in events_data:
            new_event = Event.objects.get_or_create(id=event_data['id'])[0]
            new_event.provider = event_data['provider']
            new_event.save()
            article.events.add(new_event)

        for launch_data in launchs_data:
            new_launch = Launch.objects.get_or_create(id=launch_data['id'])[0]
            new_launch.provider = launch_data['provider']
            new_launch.save()
            article.launches.add(new_launch)

        return article
