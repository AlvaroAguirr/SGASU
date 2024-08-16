from rest_framework import serializers

from .models import  Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=('__all__')
class RequestSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=(
            'applicant_name',
            'rt_objetos',
            'classroom_name',
            'rt_horario',
            'request_time'
            )
    def validate(self, data):
        """
        Validar si la hora de la solicitud está dentro del rango del horario
        y si el horario ya está reservado.
        """
        rt_horario = data.get('rt_horario')
        request_time = data.get('request_time')

        # Verifica si el horario y la hora de solicitud están presentes
        if rt_horario and request_time:
            if not (rt_horario.se_start_time <= request_time <= rt_horario.se_end_time):
                raise serializers.ValidationError(f"La hora {request_time} no está dentro del rango del horario {rt_horario}.")

        return data
    
    def to_representation(self, instance):
        # Convertir la cadena separada por comas de vuelta a una lista para la respuesta
        ret = super().to_representation(instance)
        ret['rt_objetos'] = instance.rt_objetos.split(',') if instance.rt_objetos else []
        return ret

    def to_internal_value(self, data):
        # Convertir la lista de vuelta a una cadena separada por comas antes de guardar
        if 'rt_objetos' in data and isinstance(data['rt_objetos'], list):
            data['rt_objetos'] = ','.join(data['rt_objetos'])
        return super().to_internal_value(data)
