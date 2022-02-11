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
