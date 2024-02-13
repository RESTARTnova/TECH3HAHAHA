from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lineman.serializes import ReportsSerializer, UsersSerializer
from lineman.models import Users
# Create your views here.
def index(request):
    return render(request, 'index.html')
class AuthAPI(APIView):
    def get(self, request):
        print('GET')
        #do something with 'GET' method
        return Response("Авторизация")
    def post(self,request):
        print('')
        print('AuthAPI request.data = ', end='')
        print(request.data)
        login = request.data.get('login')
        password = request.data.get('password')
        try:
            user = Users.objects.get(login=login,password=password)
            serializer = UsersSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response("Неправильный логин или пароль", status=status.HTTP_400_BAD_REQUEST)
    
class ReportCreateAPI(APIView):
    def get(self, request):
        #do something with 'GET' method
        return Response("Отчёт")
    def post(self,request):
        login = request.data.get('login')
        try:
            user = Users.objects.get(login=login)
        except Users.DoesNotExist:
            return Response("Пользователя не существует", status=status.HTTP_404_NOT_FOUND)
        bypass = user.bypass
        job_title = user.job_title