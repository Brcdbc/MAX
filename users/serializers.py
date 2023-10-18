from rest_framework import serializers

from users.models import Article


class ArtisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author','content')