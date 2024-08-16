from django.urls import path

from . import views

urlpatterns = [
    path('',views.horarioListApi.as_view())
]
