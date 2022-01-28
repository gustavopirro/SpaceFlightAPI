from rest_framework import serializers
from api.models import Article
from api.models import Launch
from api.models import Event


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
