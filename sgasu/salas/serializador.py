from rest_framework import serializers

from .models import Classroom, RoomType, Building

from horario.serializador import ScheduleSerializer
from solicitud.serializador import RequestSerializer2
class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields  =(
            'id',
            'rm_type',
            'rm_description'
        )


class BuildingSerializerTosee(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields  =(
             'bg_name',
        )

class ClassroomSerializerToCreate(serializers.ModelSerializer):
    
    
    class Meta:
        model = Classroom
        fields  =(
            'id',
            'cm_name',
            'cm_furniture',
            'cm_type',
            'cm_description',
            'cm_manager',
            'cm_roof',
            
        )

 

    
class ClassroomSerializer(serializers.ModelSerializer):
    reservacion=RequestSerializer2(many=True,source='salonespedi')
    cm_roof=BuildingSerializerTosee()
  #  horarios=ScheduleSerializer(many=True)
    cm_type=RoomTypeSerializer()
    class Meta:
        model = Classroom
        fields  =(
            'id',
            'cm_name',
            'cm_furniture',
            'cm_type',
            'cm_description',
            'cm_manager',
            'cm_roof',
            'horarios',
            'reservacion'

            
            
        )

    def update(self, instance, validated_data):
        cm_type_data = validated_data.pop('cm_type', None)
    
        # Actualizar los campos de Classroom
        instance.cm_name = validated_data.get('cm_name', instance.cm_name)
        instance.cm_furniture = validated_data.get('cm_furniture', instance.cm_furniture)
        instance.cm_description = validated_data.get('cm_description', instance.cm_description)
        instance.cm_manager = validated_data.get('cm_manager', instance.cm_manager)
        instance.cm_roof = validated_data.get('cm_roof', instance.cm_roof)
    
        if cm_type_data:
        # Aquí podrías actualizar el RoomType relacionado si es necesario
        # Por ejemplo, si `cm_type` es un campo anidado que debe actualizarse
            cm_type = instance.cm_type
            cm_type.rm_type = cm_type_data.get('rm_type', cm_type.rm_type)
            cm_type.save()

        instance.save()
        return instance
    




class BuildingSerializer(serializers.ModelSerializer):

    salones = ClassroomSerializer(many=True, source='edificio')
    class Meta:
        model = Building
        fields  =(
             'id',
             'bg_name',
             'bg_description',
             'salones',
        )