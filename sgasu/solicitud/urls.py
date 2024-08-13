from django.urls import path

from . import views

urlpatterns = [
    path('solicitud/',views.PeticionListApi.as_view())
]
