from rest_framework import serializers
from tpm.models import Faults

class FaultsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    user = serializers.CharField(max_length=30)
    rfid = serializers.CharField(max_length=16)
    fault = serializers.CharField(max_length=255)
    tag = serializers.CharField(max_length=255)
    data_time = serializers.DateTimeField(format='%Y-%m-%d/%H:%M:%S',required=False)
    class Meta:
        model = Faults
        fields = ('id','user','rfid','fault','tag','data_time')
