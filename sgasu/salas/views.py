from rest_framework import viewsets
from .serializador import  ClassroomSerializer, RoomTypeSerializer, BuildingSerializer,ClassroomSerializerToCreate
from .models import Classroom, RoomType, Building


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )


# class ClassroomViewSet(viewsets.ModelViewSet):
#     queryset =  Classroom.objects.all()
#     serializer_class= ClassroomSerializer

# class RoomtypeViewSet(viewsets.ModelViewSet):
#     queryset =  RoomType.objects.all()
#     serializer_class= RoomTypeSerializer

# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset =  Building.objects.all()
#     serializer_class= BuildingSerializer




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



    #lista de vistas de salones     
class salonListApi(ListAPIView):
    serializer_class= ClassroomSerializer
    def get_queryset(self):
        return Classroom.objects.filter(cm_roof=self.kwargs['edificio_pk'])
    
class salonDetailApi(RetrieveAPIView):

    serializer_class=ClassroomSerializer
    def get_queryset(self):
        return Classroom.objects.filter(cm_roof=self.kwargs['edificio_pk'])
    
class salonCreateApi(CreateAPIView):
    serializer_class=ClassroomSerializerToCreate


class SalonModificarApi(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def perform_update(self, serializer):
        # Obtener el edificio específico utilizando el 'edificio_pk' de la URL
        edificio = Classroom.objects.get(pk=self.kwargs['edificio_pk'])
        # Actualizar el salón con el edificio asociado
        serializer.save(edificio=edificio)

    def get_queryset(self):
        # Filtrar los salones por el edificio específico
        return Classroom.objects.filter(cm_roof=self.kwargs['edificio_pk'])


class SalonDeleteApi(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        # Filtrar salones por el edificio específico
        return Classroom.objects.filter(cm_roof=self.kwargs['edificio_pk'])
    
