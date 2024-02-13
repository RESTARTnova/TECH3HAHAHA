from rest_framework import serializers
from lineman.models import Bypass, Reports, Systems, Users

class SystemsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Systems
      fields = '__all__'

class BypassSerializer(serializers.ModelSerializer):
    class Meta:
       model = Bypass
       fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=128,required=False)
    password = serializers.CharField(max_length=255,required=False)
    class Meta:
       model = Users
       fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Reports
      fields = '__all__'


    