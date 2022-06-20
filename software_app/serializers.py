from rest_framework import serializers
from software_app.models import Software, Person, SortOfSoftware, TypeOfSoftware


class SoftwareSerializer(serializers.ModelSerializer):
    """Serializing all the Software"""
    class Meta:
        model = Software
        fields = ('id', 'name', 'description')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email')


class SortOfSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortOfSoftware
        fields = ('id', 'name', 'description_sort')


class TypeOfSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfSoftware
        fields = ('id', 'name', 'description_type')