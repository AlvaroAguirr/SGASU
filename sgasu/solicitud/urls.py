from django.urls import path

from . import views

urlpatterns = [
    path('api/solicitud/',views.PeticionListApi.as_view())
]
