from django.urls import path

from . import views

urlpatterns = [
     path('',views.PeticionListApi.as_view()),
     path('create',views.peticionCreateApi.as_view()),
     path('detail/<pk>',views.peticionDetailApi.as_view()),
     path('delete/<pk>',views.peticionDeleteApi.as_view()),
     path('modificar/<pk>',views.peticionModificar.as_view()),
]
