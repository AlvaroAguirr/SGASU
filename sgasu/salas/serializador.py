from rest_framework import serializers

from .models import Classroom, RoomType, Building



class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields  ='__all__'



class ClassroomSerializer(serializers.ModelSerializer):
    
    cm_type=RoomTypeSerializer()
    
    class Meta:
        model = Classroom
        fields  =(
            'cm_name',
            'cm_furniture',
            'cm_type',
            'cm_description',
            'cm_manager',
            'cm_roof'
        )


class BuildingSerializer(serializers.ModelSerializer):

    Salones = ClassroomSerializer(many=True, read_only=True, source='edificio')
    class Meta:
        model = Building
        fields  =(
             'id',
             'bg_name',
             'bg_description',
             'Salones',
        )