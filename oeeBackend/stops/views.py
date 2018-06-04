from .models import Stop
from rest_framework.decorators import api_view
from .serializer import StopSerializer
from rest_framework.response import Response


# Create your views here.
@api_view(['get'])
def fetch_stops(request):
    # fecth all the stop objects
    stops = Stop.objects.all()
    # send the stop object as a response
    # serialize the stops
    serializer = StopSerializer(stops, many=True)
    # return response using rest_framework's response
    return Response(serializer.data)
