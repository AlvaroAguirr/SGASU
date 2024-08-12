from django.urls import path

from . import views

urlpatterns = [
    path('api/horario/',views.horarioListApi.as_view())
]
