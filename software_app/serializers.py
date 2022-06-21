from rest_framework import serializers
from software_app.models import Software, Person, SortOfSoftware, TypeOfSoftware, MySoftware, SoftRequest, \
    BorrowSoftware


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


class MySoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySoftware
        fields = '__all__'


class SoftRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftRequest
        fields = '__all__'


class BorrowSoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowSoftware
        fields = '__all__'