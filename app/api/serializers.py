from rest_framework import serializers


class DealFileSerializer(serializers.Serializer):
    file = serializers.FileField()
