from .models import Stop
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

# def stops_list(request):
#     # fecth all the stop objects
#     stops = Stop.objects.all()
#     # send the stop object as a response
#     # serialize the stops
#     serializer = StopSerializer(stops, many=True)
#     # return response using rest_framework's response
#     return Response(serializer.data)
# Create your views here.
# @api_view(['get'])
# def stops_list(request):
#     # fecth all the stop objects
#     stops = Stop.objects.all()
#     # send the stop object as a response
#     # serialize the stops
#     serializer = StopSerializer(stops, many=True)
#     # return response using rest_framework's responsedef stops_list(request):
#     # fecth all the stop objects
#     stops = Stop.objects.all()
#     # send the stop object as a response
#     # serialize the stops
#     serializer = StopSerializer(stops, many=True)
#     # return response using rest_framework's response
#     return Response(serializer.data)
#     return Response(serializer.data)
@api_view(['GET', 'POST'])
def stops_list(request):
    """
    List all products, or create a new product.
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

