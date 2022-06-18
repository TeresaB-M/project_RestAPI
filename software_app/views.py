from rest_framework import generics

from software_app.models import Software
from software_app.serializers import SoftwareSerializer


class SoftwareListView(generics.ListCreateAPIView):
    """Returns a list of software"""

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
