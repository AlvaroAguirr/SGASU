from .serializador import RequestSerializer
from  .models import Request

from rest_framework.generics import ListAPIView

class PeticionListApi(ListAPIView):
    serializer_class =RequestSerializer
    def get_queryset(self):
        return Request.objects.all()
    

# Create your views here.
