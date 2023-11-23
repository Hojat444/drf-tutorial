from rest_framework import serializers
from .models import Concept, Relationship

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['id', 'name', 'color']

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ['id', 'origin', 'destination', 'color']
