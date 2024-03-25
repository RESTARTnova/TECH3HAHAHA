import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lineman.serializes import ActionSerializer, ActionsSerializer, DurabilitySerializer, JobsSerializer, LogsSerializer, NFCSerializer, ReportsRoomSerializer, RoomsSerializer, RoomsSpecialSerializer, UsersSerializer
from lineman.models import  NFC, Actions, ActionsRoom, Durability,  Job_titles, Logs, ReportsRoom, Rooms, RoomsReport, Users
from django.db.models import Q

# Перевод данных от телефона
def descriptor(data):
    eex = str(data)
    rooms = []
    remarks_id = []
    room_id = []
    logs_mass = []
    room = -1
    user_job = data.get('job')
    start_time = data.get('start_time')
    stop_time = data.get('stop_time')
    for i in data.get('logs'):
        logs_mass.append(Logs.objects.create(logl=i.get('log'),timel=i.get('time')).pk)
    for i in range(len(data.get('rooms'))):
        rooms.append(data.get('rooms')[i])
    for i in rooms:
        name_room = i.get('name')
        remarks_id = []
        for j in i.get('remarks'):
            remarks_id.append(ActionsRoom.objects.create(name_r=j.get('name'),remark_r=j.get('note')).pk)
        room = RoomsReport.objects.create(room_r=name_room)
        room.actions_r.set(remarks_id)
        room_id.append(room.pk)
    rom = ReportsRoom.objects.create(rep_name=user_job,rep_start_time=start_time,rep_stop_time=stop_time,rep_string=eex.replace('\'','\"')).pk
    ReportsRoom.objects.get(pk=rom).rep_rooms.set(room_id)
    ReportsRoom.objects.get(pk=rom).rep_logs.set(logs_mass)

def incriptor(data):
    result = []
    yes_intermidate = []
    aaaaa = []
    job = data.get('work_rooms')
    user = Job_titles.objects.get(job_name=job)
    actions = dict(JobsSerializer(user).data).get('job_action')
    rooms = Rooms.objects.all()
    room = (RoomsSerializer(rooms,many=True).data)
    for i in room:
        yes_intermidate.clear()
        for j in actions:
            if j in i.get('room_action'):
                yes_intermidate.append(j)
                if i not in result:
                    result.append(i)
        if len(yes_intermidate) != 0:
            aer = yes_intermidate.copy()
            aaaaa.append({'action' : aer})
    result.append({'actions':aaaaa})
    return result

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AuthAPI(APIView):
    def get(self, request):
        user1 = Users.objects.all()
        serialize1 = UsersSerializer(user1, many=True)
        return Response({ '1' : serialize1.data})
    def post(self,request):
        if 'login' in request.data and 'password' in request.data:
            login = request.data.get('login')
            password = request.data.get('password')
            try:
                user = Users.objects.get(login=login,password=password)
                serializer = UsersSerializer(user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                return Response("Неправильный логин или пароль", status=status.HTTP_400_BAD_REQUEST)
        if 'nfc_id' in request.data:
            idf = request.data.get('nfc_id')
            try:
                nfd = NFC.objects.get(nfc_code=idf).pk
                userw = Users.objects.get(nfc_id=nfd)
                serializer1 = UsersSerializer(userw)
                return Response(serializer1.data)
            except:
                return Response('KYS',status=status.HTTP_401_UNAUTHORIZED)
        return Response('undefined',status=status.HTTP_400_BAD_REQUEST)
    
class JobTitlesAPI(APIView):
    def get(self,request):
        jobs = Job_titles.objects.all()
        serialize1 = JobsSerializer(jobs, many=True)
        return Response({ '1' : serialize1.data})
    def post(self, request):
        job = request.data.get('job')
        jobs = Job_titles.objects.get(pk=job)
        serializer1 = JobsSerializer(jobs)
        return Response(serializer1.data)

class ActionAPI(APIView):
    def get(self, request):
        actions = Actions.objects.all()
        serialize1 = ActionSerializer(actions, many=True)
        return Response({ '1' : serialize1.data})
    def post(self, request):
        actions = []
        action = request.data.get('actions')
        for i in action:
            actions.append(Actions.objects.get(pk=i))
        serializer1 = ActionSerializer(actions, many=True)
        return Response(serializer1.data)

class ReportsRoomAPI(APIView):
    def get(self,request):
        report = ReportsRoom.objects.all()
        serializer1 = ReportsRoomSerializer(report,many=True)
        return Response(serializer1.data)
    def post(self, request):
        data = request.data
        descriptor(data)
        return Response('Post complete',status=status.HTTP_201_CREATED)

class RoomsAPI(APIView):
    def get(self,request):
        rooms = Rooms.objects.all()
        serializer1 = RoomsSerializer(rooms, many=True)
        return Response({ '1' : serializer1.data})
    def post(self, request):
        info = incriptor(request.data)
        json1 = json.dumps(info)
        return Response(json1)

class ReportsRoomFilterAPI(APIView):
    def get(self,request):
        reports = ReportsRoom.objects.all()
        serializer1 = ReportsRoomSerializer(reports, many=True)
        return Response({ '1' : serializer1.data})
    def post(self,request):
        date_begin = request.data['rep_start_time'] + " 00:00:00.00"
        date_end = request.data['rep_stop_time'] + " 23:59:59.99"
        reports = ReportsRoom.objects.filter(Q(rep_start_time__gte=date_begin) & Q(rep_stop_time__lte=date_end))
        serializer1 = ReportsRoomSerializer(reports,many=True)
        return Response(serializer1.data)

class RoomsReportAPI(APIView):
    def post(self, request):
        rooms = []
        eoom = request.data.get('room')
        for i in eoom:
            rooms.append(RoomsReport.objects.get(pk=i))
        serializer1 = RoomsSpecialSerializer(rooms, many=True)
        return Response(serializer1.data)

class ActionsReportAPI(APIView):
    def post(self, request):
        actions = []
        action = request.data.get('action')
        for i in action:
            actions.append(ActionsRoom.objects.get(pk=i))
        serializer1 = ActionsSerializer(actions, many=True)
        return Response(serializer1.data)

class DurabilityAPI(APIView):
    def get(self,request):
        duras = Durability.objects.all()
        serializer1 = DurabilitySerializer(duras,many=True)
        return Response(serializer1.data)
    def post(self, request):
        data = request.data.get('dur')
        dura = Durability.objects.get(pk=data)
        serializer1 = DurabilitySerializer(dura)
        return Response(serializer1.data)

class NFCAPI(APIView):
    def get(self,request):
        nfcs = NFC.objects.all()
        serializer1 = NFCSerializer(nfcs,many=True)
        return Response(serializer1.data)
    def post(self,request):
        mass = []
        data = request.data.get('ids')
        for i in data:
            mass.append(NFC.objects.get(pk=i))
        serializer1 = NFCSerializer(mass,many=True)
        return Response(serializer1.data)

class LogsAPI(APIView):
    def get(self, request):
        logs = Logs.objects.all()
        serializer1 = LogsSerializer(logs,many=True)
        return Response(serializer1.data)
    def post(self, request):
        data = request.data.get('ids')
        mass = []
        for i in data:
            mass.append(Logs.objects.get(pk=i))
        serializer1 = LogsSerializer(mass,many=True)
        return Response(serializer1.data)


# {"start_time":"2024-03-22T14:16:25.457Z","job":"Слесарь-ремонтник(гидравлик)","stop_time":"2024-03-22T14:18:23.567Z","rooms":[{"name":"Кабина электрод печи №4","remarks":[{"empty":false,"name":"Проверить чистоту в кабине электродов.","note":"Gods"},{"empty":false,"name":"Проверить визуальную систему трубопроводов и соединений на предмет утечек рабочей жидкости. Течи не допускаются.","note":"852"}]}],"logs":[{"time":"12:16:25","log":"JKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"},{"time":"23:40:23","log":"ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"}]}
# {"work_rooms":"Cлесарь-ремонтник"}
# {"work_rooms":"Cлесарь-ремонтник(гидравлик)"}