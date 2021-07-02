from rest_framework import serializers
from ranking.models import Score, RankingUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingUser
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'