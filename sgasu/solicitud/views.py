from .serializador import RequestSerializer, RequestSerializer2
from  .models import Request


from rest_framework.generics import (

ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )



class PeticionListApi(ListAPIView):
    serializer_class =RequestSerializer2
    def get_queryset(self):
        return Request.objects.all()
    

class peticionCreateApi(CreateAPIView):
    serializer_class=RequestSerializer2

class peticionDetailApi(RetrieveAPIView):
    serializer_class=RequestSerializer
    queryset=Request.objects.filter()


class peticionDeleteApi(DestroyAPIView):
    serializer_class=RequestSerializer
    queryset=Request.objects.filter()


class peticionModificar(RetrieveUpdateAPIView):
    queryset= Request.objects.all()
    serializer_class=RequestSerializer2



