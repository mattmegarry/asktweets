from rest_framework import serializers
from .models import MP, Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['name']

class MPSerializer(serializers.ModelSerializer):
    party = serializers.StringRelatedField()

    class Meta:
        model = MP
        fields = ['id', 'name', 'party', 'constituency']

