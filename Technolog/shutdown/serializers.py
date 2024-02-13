from dataclasses import fields
# from typing import Required
from rest_framework import serializers
from shutdown.models import Shutdown , ClassShutdown, TypeShutdown, FactorShutdown
# TypeShutdown, ClassShutdown, FactorShutdown

class ShutdownSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    date_begin = serializers.DateTimeField( format="%Y.%m.%d %H:%M:%S", required=False)
    
    date_end = serializers.DateTimeField( format="%Y.%m.%d %H:%M:%S", required=False)
    interval = serializers.DurationField(required=False)
    agregate_name = serializers.CharField(max_length=255,required=False)
    flag_classification = serializers.BooleanField(required=False) # класифицирован ли простой
    class_shutdown = serializers.SlugRelatedField(slug_field='class_shutdown', queryset=ClassShutdown.objects, required=False)
    type_shutdown = serializers.SlugRelatedField(slug_field='type_shutdown', queryset=TypeShutdown.objects, required=False) 
    factor_shutdown = serializers.SlugRelatedField(slug_field='factor_shutdown', queryset=FactorShutdown.objects, required=False)
    commentary = serializers.CharField(required=False) 
    machine = serializers.CharField(max_length=255,required=False) 
    node = serializers.CharField(max_length=255,required=False)
    element = serializers.CharField(max_length=255,required=False) 
    detail = serializers.CharField(max_length=255,required=False)
    href_documentation = serializers.CharField(max_length=255,required=False)



    def create(self, validated_data):

        return Shutdown.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.date_begin =           validated_data.get('date_begin', instance.date_begin)
        instance.date_end =             validated_data.get('date_end', instance.date_end)
        instance.interval =             validated_data.get('interval', instance.interval)
        instance.agregate_name =        validated_data.get('agregate_name', instance.agregate_name)
        instance.flag_classification =  validated_data.get('flag_classification', instance.flag_classification)
        # print('instance.class_shutdown = '+ instance.class_shutdown)
        # instance.class_shutdown = int(instance.class_shutdown)
        instance.class_shutdown =       validated_data.get('class_shutdown', instance.class_shutdown)
        instance.type_shutdown =        validated_data.get('type_shutdown', instance.type_shutdown)
        instance.factor_shutdown =      validated_data.get('factor_shutdown', instance.factor_shutdown)
        instance.commentary =           validated_data.get('commentary', instance.commentary)
        instance.machine =              validated_data.get('machine', instance.machine)
        instance.node =                 validated_data.get('node', instance.node)
        instance.element =              validated_data.get('element', instance.element)
        instance.detail =               validated_data.get('detail', instance.detail)
        instance.href_documentation =   validated_data.get('href_documentation', instance.href_documentation)
        instance.save()
        return instance
    

    
    class Meta :
        model = Shutdown
        fields = '__all__'
        # read_only_fields = ['date_begin',]
        # fields = ('id',
        #           'date_begin_test',
        #            'date_begin',
        #            'date_end',
        #            'agregate_name', 
        #            'flag_classification', 
        #            'class_shutdown', 
        #            'type_shutdown', 
        #            'factor_shutdown', 
        #            'commentary', 
        #            'machine', 
        #            'node', 
        #            'element', 
        #            'detail', 
        #            'href_documentation')
    
    # def to_representation(self, instance):
    #     primitive_repr = super(ShutdownSerializer, self).to_representation(instance)
    #     primitive_repr['начало простоя'] = primitive_repr['date_begin']
    #     # primitive_repr.pop('date_begin')
    #     return primitive_repr
        
class ClassShutdownSerializer(serializers.ModelSerializer):
    class Meta :
        model = ClassShutdown
        fields = '__all__'


class TypeShutdownSerializer(serializers.ModelSerializer):

    class Meta:
        model= TypeShutdown
        fields = '__all__'


class FactorShutdownSerializer(serializers.ModelSerializer):

    class Meta:
        model = FactorShutdown
        fields = '__all__'