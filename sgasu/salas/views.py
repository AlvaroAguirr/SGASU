from rest_framework import viewsets
from .serializador import  ClassroomSerializer, RoomTypeSerializer, BuildingSerializer
from .models import Classroom, RoomType, Building



class ClassroomViewSet(viewsets.ModelViewSet):
    queryset =  Classroom.objects.all()
    serializer_class= ClassroomSerializer

class RoomtypeViewSet(viewsets.ModelViewSet):
    queryset =  RoomType.objects.all()
    serializer_class= RoomTypeSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset =  Building.objects.all()
    serializer_class= BuildingSerializer