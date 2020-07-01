from rest_framework import serializers

from item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'name',
            'description'
        ]

    def validate_description(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("Description should have a max of 1000")
        return value