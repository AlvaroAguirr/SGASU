from django.urls import path, include
from rest_framework import routers

from . import views

urlpatterns = [
     
     path('',views.edificioListApi.as_view()),
     path('create',views.edificioCreateApi.as_view()),
     path('detail/<pk>',views.edificioDetailApi.as_view()),
     path('delete/<pk>',views.edificioDeleteApi.as_view()),
     path('update/<pk>',views.edificioUpdateApi.as_view()),
     path('modificar/<pk>',views.edificioModificar.as_view()),
    
     path('<int:edificio_pk>/salones/',views.salonListApi.as_view()),
     path('salones/create',views.salonCreateApi.as_view()),
     path('<int:edificio_pk>/salones/<pk>',views.salonDetailApi.as_view()),
     path('<int:edificio_pk>/salones/modificar/<pk>',views.SalonModificarApi.as_view()),
     path('<int:edificio_pk>/salones/delete/<pk>',views.SalonDeleteApi.as_view()),

]