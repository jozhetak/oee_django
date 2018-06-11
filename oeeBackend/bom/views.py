from rest_framework import generics

from .models import Bom
from .serializer import BomSerializer

# Create your views here.

class BomList(generics.ListCreateAPIView):
    queryset = Bom.objects.all()
    serializer_class = BomSerializer

class BomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bom.objects.all()
    serializer_class = BomSerializer

