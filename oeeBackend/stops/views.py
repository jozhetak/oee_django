from .models import Stop
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

@api_view(['GET', 'POST'])
def stops_list(request):
    """
    List all stops, or create a new Stop.
    """
    if request.method == 'GET':

        stops = Stop.objects.all()
        serializer = StopSerializer(stops,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stops_detail(request, pk):
    """
    Retrieve, update or delete anstop instance.
    """
    try:
        stop = Stop.objects.get(pk=pk)
    except Stop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StopSerializer(stop,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StopSerializer(stop, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)