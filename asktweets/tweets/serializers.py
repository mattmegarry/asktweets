from rest_framework import serializers
from .models import MP, Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['name']

class MPSerializer(serializers.ModelSerializer):
    party = serializers.StringRelatedField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = MP
        fields = ['id', 'name', 'party', 'constituency', 'label']

    def get_label(self, obj):
        return f"{obj.name} - {obj.constituency}"

