from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Concept, Relationship
from .serializers import ConceptSerializer, RelationshipSerializer

@api_view(['GET', 'POST'])
def concept_list(request):
    if request.method == 'GET':
        concepts = Concept.objects.all()
        serializer = ConceptSerializer(concepts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConceptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def concept_detail(request, pk):
    try:
        concept = Concept.objects.get(pk=pk)
    except Concept.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConceptSerializer(concept)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConceptSerializer(concept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        concept.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def relationship_list(request):
    if request.method == 'GET':
        relationships = Relationship.objects.all()
        serializer = RelationshipSerializer(relationships, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RelationshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def relationship_detail(request, pk):
    try:
        relationship = Relationship.objects.get(pk=pk)
    except Relationship.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RelationshipSerializer(relationship)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RelationshipSerializer(relationship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        relationship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
