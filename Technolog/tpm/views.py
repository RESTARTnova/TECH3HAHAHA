from django.shortcuts import render
from django.http import HttpResponse
from tpm.models import Faults
from tpm.serialize import FaultsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return HttpResponse("ok")

class WriteFaults(APIView):
    def post(self,request,format=None):
        serializer = FaultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class GetFaults(APIView):
    def get(self, request,format=None):
        queryset = Faults.objects.all()
        serializer_class = FaultsSerializer(queryset,many=True)
        return Response({'faults' : serializer_class.data})
    