from rest_framework import viewsets
from ranking.models import Score, RankingUser
from ranking.serializers import ScoreSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for users"""
    queryset = RankingUser.objects.all()
    serializer_class = UserSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    """API endpoint for scores"""
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
