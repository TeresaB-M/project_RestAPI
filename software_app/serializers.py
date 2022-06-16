from rest_framework import serializers
from software_app.models import Software


class SoftwareSerializer(serializers.ModelSerializer):
    """Serializing all the Software"""
    class Meta:
        model = Software
        fields = ('name', 'description')