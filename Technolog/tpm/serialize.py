from rest_framework import serializers
from tpm.models import Faults

class FaultsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=255)
    rfid = serializers.CharField(max_length=255)
    fault = serializers.CharField(max_length=255)
    tag = serializers.CharField(max_length=255)
    data_time = serializers.CharField(max_length=255)
    data_time_now = serializers.CharField(max_length=255)
   
    class Meta:
        model = Faults
        fields = '__all__'
   