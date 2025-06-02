from rest_framework import serializers


class FakeDataRequestSerializer(serializers.Serializer):
    fields = serializers.ListField(child=serializers.CharField(), required=True)
    quantity = serializers.IntegerField(min_value=1, default=1)
