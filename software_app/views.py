from rest_framework import generics

from software_app.models import Software, Person, SortOfSoftware, TypeOfSoftware, MySoftware, SoftRequest
from software_app.serializers import SoftwareSerializer, PersonSerializer, SortOfSoftwareSerializer
from software_app.serializers import TypeOfSoftwareSerializer, MySoftwareSerializer, SoftRequestSerializer


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


class SortOfSoftwareListView(generics.ListCreateAPIView):
    queryset = SortOfSoftware.objects.all()
    serializer_class = SortOfSoftwareSerializer


class SortOfSoftwareView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SortOfSoftware.objects.all()
    serializer_class = SortOfSoftwareSerializer


class TypeOfSoftwareListView(generics.ListCreateAPIView):
    queryset = TypeOfSoftware.objects.all()
    serializer_class = TypeOfSoftwareSerializer


class TypeOfSoftwareView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeOfSoftware.objects.all()
    serializer_class = TypeOfSoftwareSerializer


class MySoftwareListView(generics.ListCreateAPIView):
    queryset = MySoftware.objects.all()
    serializer_class = MySoftwareSerializer


class MySoftwareView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MySoftware.objects.all()
    serializer_class = MySoftwareSerializer


class SoftRequestListView(generics.ListCreateAPIView):
    queryset = SoftRequest.objects.all().order_by('id')
    serializer_class = SoftRequestSerializer
