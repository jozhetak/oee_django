from rest_framework import generics

from .models import JobOrderDetail
from .serializer import JobOrderDetailSerializer

# Create your views here.

class JobOrderDetailList(generics.ListCreateAPIView):
    queryset = JobOrderDetail.objects.all()
    serializer_class = JobOrderDetailSerializer

class JobOrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOrderDetail.objects.all()
    serializer_class = JobOrderDetailSerializer

