from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testing.serializers import ForeignKeyTestS, ForeignKeyTestFS
from testing.models import ForeignKeyTest, ForeignKeyTestF

# Create your views here.

def testing(request):

    return render(request)

class GetTestingForeignKey(APIView):
    def get(self, request,format=None):
        # print (request.GET)
        queryset = ForeignKeyTestF.objects.all()
        print('on backend')
        serializer_class = ForeignKeyTestFS(queryset,many=True)
        return Response({'ForeignKeyTestF' : serializer_class.data})

class GetTestingForeignKeyF(APIView):
    def get(self, request,format=None):
        # print (request.GET)
        queryset = ForeignKeyTest.objects.all()
        print('on backend 2')
        serializer_class = ForeignKeyTestS(queryset,many=True)
        return Response({'ForeignKeyTest' : serializer_class.data})

class GetTestingForeignKeyIdFilter(APIView):
    def get(self,request,format=None):#
        queryset = ForeignKeyTestF.objects.all().filter(foreign_key_test__name__contains="NAME_1")
        serializer_class = ForeignKeyTestFS(queryset,many=True)
        return Response({'ForeignKeyTestIdFilter' : serializer_class.data})