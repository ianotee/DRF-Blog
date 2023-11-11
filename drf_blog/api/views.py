from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET'])
def urls_list(request):

    urls_list ={
        'list': 'list',
        'Details': 'Details/<str:pk>/',
        'create': 'create/',
        'update':'update/<str:pk>/',
        'delete': 'delete/<str:pk>/',
        'Information':'This are the api  endpoints that I will create',
    }

    return Response(urls_list)

#list all Objects.
@api_view(['GET'])
def list(request):
    list =Person.objects.all()
    serializer =PersonSerializer(list, many=True)
    return Response(serializer.data)

#Retrieves
@api_view(['GET'])
def Details(request, pk):
    list =Person.objects.get(id=pk)
    serializer =PersonSerializer(list , many=False)
    return Response(serializer.data)

# Creates
@api_view(['POST'])
def create(request):
    serializer=PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

# Updates
@api_view(['PUT'])
def update(request,pk):
    list =Person.objects.get(id=pk)
    serializer = PersonSerializer(data =request.data, instance=list)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)



# Deletes
@api_view(['DELETE'])
def delete(request, pk):
    list =Person.objects.get(id=pk)
    list.delete()
    return Response("The Object was deleted successfully.")