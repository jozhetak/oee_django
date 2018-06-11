from rest_framework import generics

from .models import Workstation
from .serializer import WorkstationSerializer

# Create your views here.

class WorkstationList(generics.ListCreateAPIView):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

class WorkstationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workstation.objects.all()
    serializer_class = WorkstationSerializer

