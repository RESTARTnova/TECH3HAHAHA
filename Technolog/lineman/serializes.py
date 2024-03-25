from dataclasses import fields
from rest_framework import serializers
from lineman.models import   NFC, Actions, ActionsRoom, Durability,  Job_titles, Logs, ReportsRoom, Rooms, RoomsReport, Users


class UsersSerializer(serializers.ModelSerializer):
      class Meta:
         model = Users
         fields = '__all__'

class ReportsRoomSerializer(serializers.ModelSerializer):
   class Meta:
      model = ReportsRoom
      fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Job_titles
      fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Actions
      fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Rooms
      fields = '__all__'

class RoomsSpecialSerializer(serializers.ModelSerializer):
   class Meta:
      model = RoomsReport
      fields = '__all__'

class ActionsSerializer(serializers.ModelSerializer):
   class Meta:
      model = ActionsRoom
      fields = '__all__'

class DurabilitySerializer(serializers.ModelSerializer):
   class Meta:
      model = Durability
      fields = '__all__'

class NFCSerializer(serializers.ModelSerializer):
   class Meta:
      model = NFC
      fields = '__all__'

class LogsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Logs
      fields = '__all__'
