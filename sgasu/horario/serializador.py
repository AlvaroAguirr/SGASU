from rest_framework import serializers

from .models import Schedule
from salas.serializador import ClassroomSerializer

class ScheduleSerializer(serializers.ModelSerializer):

    se_classroom=ClassroomSerializer()

    class Meta:
        model= Schedule
        fields=(
            'id',
            'se_day',
            'se_start_time',
            'se_end_time',
            'se_classroom'
        )