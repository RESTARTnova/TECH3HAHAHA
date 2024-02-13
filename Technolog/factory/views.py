from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from factory.models import Machines, Nodes, Elements, Details
from rest_framework.response import Response
from factory.serializes import MachinesSerializer, NodesSerializer, ElementSerializer, DetailsSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')
class testResp(APIView):
    def get(self, request):
        # queryset = {"test_data": [
        #     {"name":"john"},
        #     {"last_name":"kgfsjh"}
        # ]}
        return Response({"name": "john"})
    
class MachineList(APIView):
    def get(self,request):
        queryset = Machines.objects.all()
        serialize_class = MachinesSerializer(queryset,many=True)
        return Response({'machines' : serialize_class.data})
    
class NodeList(APIView):
    def get(self,request):
        queryset = Nodes.objects.all()
        serialize_class = NodesSerializer(queryset,many=True)
        return Response({'nodes' : serialize_class.data})

class ElementList(APIView):
    def get(self,request):
        queryset = Elements.objects.all()
        serialize_class = ElementSerializer(queryset,many=True)
        return Response({'elements' : serialize_class.data})
    
class DetailsList(APIView):
    def get(self, request):
        queryset = Details.objects.filter()
        serialize_class = DetailsSerializer(queryset,many=True)
        return Response({'details' : serialize_class.data})

class WriteMachine(APIView):
    def post(self,request):
        serialize = MachinesSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

class WriteNode(APIView):
    def post(self,request):
        serialize = NodesSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

class WriteElement(APIView):
    def post(self,request):
        serialize = ElementSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

class WriteDetail(APIView):
    def post(self,request):
        serialize = DetailsSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)