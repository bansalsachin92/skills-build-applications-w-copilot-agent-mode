from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity, Team
from .serializers import ActivitySerializer, TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
