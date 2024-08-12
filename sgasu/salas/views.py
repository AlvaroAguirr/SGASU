from rest_framework import viewsets
from .serializador import  ClassroomSerializer, RoomTypeSerializer, BuildingSerializer
from .models import Classroom, RoomType, Building


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset =  Classroom.objects.all()
    serializer_class= ClassroomSerializer

class RoomtypeViewSet(viewsets.ModelViewSet):
    queryset =  RoomType.objects.all()
    serializer_class= RoomTypeSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset =  Building.objects.all()
    serializer_class= BuildingSerializer


#ver lista
class edificioListApi(ListAPIView):

    serializer_class= BuildingSerializer
    def get_queryset(self):
        return Building.objects.all()
    
    #crear objeto
class edificioCreateApi(CreateAPIView):
    serializer_class=BuildingSerializer

    #ver especifico
class edificioDetailApi(RetrieveAPIView):

    serializer_class=BuildingSerializer
    queryset=Building.objects.filter()
    
#para eliminar elemento especifico
class edificioDeleteApi(DestroyAPIView):

    serializer_class=BuildingSerializer
    queryset=Building.objects.filter()

class edificioUpdateApi(UpdateAPIView):
    queryset= Building.objects.all()
    serializer_class=BuildingSerializer

class edificioModificar(RetrieveUpdateAPIView):
    queryset= Building.objects.all()
    serializer_class=BuildingSerializer
