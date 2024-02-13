from rest_framework import serializers
from factory.models import Machines,Nodes,Elements,Details

class MachinesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    rfid = serializers.CharField(max_length=16)
    class Meta:
      model = Machines
      fields = ("id", "name","rfid")

class NodesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    machine = serializers.SlugRelatedField(many=False,read_only=True,slug_field='id')
    class Meta:
       model = Nodes
       fields = ("id", "name","machine")

class ElementSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    element = serializers.SlugRelatedField(many=False,read_only=True,slug_field='id')
    class Meta:
       model = Elements
       fields = ("id", "name","element")

class DetailsSerializer(serializers.ModelSerializer):
   name = serializers.CharField(max_length=255)
   detail = serializers.SlugRelatedField(many=False,read_only=True,slug_field='id')
   class Meta:
      model = Details
      fields = ("id", "name","detail")

    