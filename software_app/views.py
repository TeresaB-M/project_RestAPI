from rest_framework import generics

from software_app.models import Software, Person
from software_app.serializers import SoftwareSerializer, PersonSerializer


class SoftwareListView(generics.ListCreateAPIView):
    """Returns a list of software"""

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class PersonListView(generics.ListCreateAPIView):
    """Returns a list of person"""

    queryset = Person.objects.all().order_by('id')

    def get_serializer_class(self):
        return PersonSerializer

    def get(self, request):
        return self.list(request)


class PersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
