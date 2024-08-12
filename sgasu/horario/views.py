from .serializador import ScheduleSerializer
from .models import Schedule

from rest_framework.generics import ListAPIView

class  horarioListApi(ListAPIView):
    serializer_class = ScheduleSerializer
    def get_queryset(self):
        return Schedule.objects.all()
    

