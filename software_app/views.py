from django.shortcuts import render
from rest_framework import generics

from software_app.models import Software
from software_app.serializers import SoftwareSerializer


class SoftwareListView(generics.ListCreateAPIView):
    """Returns a list of software"""
    # model = Software
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
