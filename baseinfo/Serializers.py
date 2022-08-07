from rest_framework import serializers
from .models import DesignModels, DesignJson

class DesignModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignModels
        fields = '__all__'


class DesignJsonSerializer(serializers.ModelSerializer):
    owners_data = DesignModelsSerializer(many=True)

    class Meta:
        model = DesignJson
        fields = '__all__'

    def create(self, validated_data):
        owners_data = validated_data.pop('owners_data')
        template = DesignJson.objects.create(**validated_data)
        for owner_data in owners_data:
            DesignModels.objects.create(DesignJson_id=template, **owner_data)
        return template