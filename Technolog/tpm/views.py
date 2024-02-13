from django.shortcuts import render
from django.http import HttpResponse
from tpm.models import Faults
from tpm.serialize import FaultsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

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
    def post(self,request,format=None):
        date_begin = request.data["date_begin"]
        date_end = request.data["date_end"]
        filter = request.data["filter"]
        if filter != "None":
            filter_date = request.data["filter"]["filter_date"]
            filter_user = request.data["filter"]["filter_user"]
            filter_machine = request.data["filter"]["filter_machine"]
            if((filter_date != None and filter_date != "") and (filter_machine == None or filter_machine == "") and (filter_user == None or filter_user == "")):
                date1 = filter_date.replace("/","-") + " 00:00:00.00"
                date2 = filter_date.replace("/","-") + " 23:59:59.99"
                queryset = Faults.objects.filter(Q(data_time_now__gte=date1) & Q(data_time_now__lte=date2))
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date == None or filter_date == "") and (filter_user == None or filter_user == "") and (filter_machine != None and filter_machine != "")):
                queryset = Faults.objects.filter(rfid=filter_machine)
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date == None or filter_date == "") and (filter_user != None and filter_user != "") and (filter_machine == None or filter_machine == "")):
                queryset = Faults.objects.filter(user=filter_user)
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date != None and filter_date != "")and(filter_user != None and filter_user != "")and(filter_machine == None or filter_machine == "")):
                date1 = filter_date.replace("/","-") + " 00:00:00.00"
                date2 = filter_date.replace("/","-") + " 23:59:59.99"
                queryset = Faults.objects.filter(Q(user=filter_user) & Q(data_time_now__gte=date1) & Q(data_time_now__lte=date2))
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date != None and filter_date != "")and(filter_user == None or filter_user == "")and(filter_machine != None and filter_machine != "")):
                date1 = filter_date.replace("/","-") + " 00:00:00.00"
                date2 = filter_date.replace("/","-") + " 23:59:59.99"
                queryset = Faults.objects.filter(Q(rfid=filter_machine) & Q(data_time_now__gte=date1) & Q(data_time_now__lte=date2))
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date == None or filter_date == "")and(filter_user != None and filter_user != "")and(filter_machine != None and filter_machine != "")):
                queryset = Faults.objects.filter(Q(user=filter_user) & Q(rfid=filter_machine))
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
            if((filter_date != None and filter_date != "")and(filter_user != None and filter_user != "")and(filter_machine != None and filter_machine != "")):
                date1 = filter_date.replace("/","-") + " 00:00:00.00"
                date2 = filter_date.replace("/","-") + " 23:59:59.99"
                queryset = Faults.objects.filter(Q(user=filter_user) & Q(data_time_now__gte=date1) & Q(data_time_now__lte=date2) & Q(rfid=filter_machine))
                serializer_class = FaultsSerializer(queryset,many=True)
                return Response({'filtered_faults' : serializer_class.data})
        date_begin = date_begin.replace("/","-") + " 00:00:00.00"
        date_end = date_end.replace("/","-") + " 23:59:59.99"
        queryset = Faults.objects.filter(Q(data_time_now__gte=date_begin) & Q(data_time_now__lte=date_end))
        serializer_class = FaultsSerializer(queryset,many=True)
        return Response({'filtered_faults' : serializer_class.data})
