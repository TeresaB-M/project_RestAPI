from rest_framework import serializers
from software_app.models import Software, Person


class SoftwareSerializer(serializers.ModelSerializer):
    """Serializing all the Software"""
    class Meta:
        model = Software
        fields = ('id', 'name', 'description')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email')
