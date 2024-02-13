from ast import Global
from tarfile import NUL
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from shutdown.serializers import ShutdownSerializer, ClassShutdownSerializer, FactorShutdownSerializer, TypeShutdownSerializer
from shutdown.models import Shutdown, ClassShutdown, FactorShutdown, TypeShutdown
from factory.models import *
from datetime import datetime



# Create your views here.
# def index(request):
#     return render(request)

class GetShutdowns(APIView):
    
    #Делаем универсальный фильтр, в качестве параметров отбора в обязательном порядке должны быть????:
    
    number_agregate = '' # Имя агрегата выпадающий список
    types_shutdown = ''# Тип простоя в виде выпадающего списка, как и номер печи
    class_shutdown = ''# Вид простоя выпадающий список
    factors_shutdown = ''# факторы простоев выпадающий список
    machine ='' #
    node = ''#
    element = ''#
    detail = ''#
    
    def post(self, request, format=None):
        period_begin=''# дата начала выборки
        period_end=''#дата окончания выборки
        # print(request.data['test'])
        if 'date_begin' in request.data and 'date_end' in request.data: # Если есть данные с фронта, то используем их, иначе задаём дефолтные
            print('request.data[date_begin] = '+ str(request.data['date_begin']))
            print('request.data[date_end] = '+ str(request.data['date_end']))
            period_begin = request.data['date_begin']+" 00:00:00" 
            period_end =request.data['date_end']+" 23:59:00" 
        
        queryset = Shutdown.objects.filter(date_end__range=(period_begin, period_end))
        serializer_class = ShutdownSerializer(queryset, many=True)
        my_data = serializer_class.data
        if(my_data):
            # print('my_data = '+ str(my_data))
            for i in my_data:
                i['Название агрегата']=i.pop('agregate_name')
                i['Начало простоя']=i.pop('date_begin')
                i['Окончание простоя']=i.pop('date_end')           
                i['продолжительность']=i.pop('interval')
                i['Классификация']=i.pop('flag_classification')
                i['Вид простоя']=i.pop('class_shutdown')
                i['Тип простоя']=i.pop('type_shutdown')
                i['Фактор простоя']=i.pop('factor_shutdown')
                i['Примечание']=i.pop('commentary')
                i['Машина']=i.pop('machine')
                i['Узел']=i.pop('node')
                i['Элемент']=i.pop('element')
                i['Деталь']=i.pop('detail')
                i['Документация']=i.pop('href_documentation')
            return Response({'Shutdowns': my_data})
        else: return Response({})



class getClassShutdowns(APIView):

    

    def post(self, request, format=None):

      
        
        print('request = ' + str(request.data))

            

        if request.data['lvl']==0:
            queryset = ClassShutdown.objects.all()
            serializer_class = ClassShutdownSerializer(queryset, many=True)
            my_data = serializer_class.data
            print(my_data)
            return Response({'ClassShutdown': my_data})
        elif request.data['change']=='init':
            return Response({})
        else:
            if request.data['lvl']==1 and request.data['change'] !='':
                queryset = ClassShutdown.objects.get(class_shutdown = request.data['change'])
               
                # print(TypeShutdownSerializer(queryset.typeshutdown_set.all(), many=True).data)
                my_data = TypeShutdownSerializer(queryset.typeshutdown_set.all(), many=True).data
                print(my_data)
                return Response({'TypeShutdown': my_data})
            if request.data['lvl']==2 and request.data['change'] !='':
                queryset = TypeShutdown.objects.get(type_shutdown = request.data['change'])
               
                # print(FactorShutdownSerializer(queryset.factorshutdown_set.all(), many=True).data)
                my_data = FactorShutdownSerializer(queryset.factorshutdown_set.all(), many=True).data
                print(my_data)   
                return Response({'FactorShutdown': my_data})
            return Response({})  


class ShutdownDetail(APIView):

    def get_object(self, pk):
        try:
            # print(pk)
            return Shutdown.objects.get(pk=pk)
        except Shutdown.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        shutdown = self.get_object(pk)
        serializer = ShutdownSerializer(shutdown)
        return Response(serializer.data)
    
    def put(self, request,  format=None):
        print('enter')
        print(request.data)
        shutdown = self.get_object(pk=request.data['classifications']['id'])
        
        print(shutdown.date_begin)
        serializer = ShutdownSerializer(shutdown, data= request.data['classifications'])
        # print(serializer.errors)
        # serializer.is_valid(raise_exception=True)
        
        if serializer.is_valid():
            print('прошли валидацию')
            serializer.save()
            print('прошли валидацию')
            print(serializer.errors)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

            
    