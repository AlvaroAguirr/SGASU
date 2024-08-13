from django.urls import path

from . import views

urlpatterns = [
    path('horario/',views.horarioListApi.as_view())
]
