from django.urls import path, include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'Classroom',views.ClassroomViewSet)
router.register(r'RoomType',views.RoomtypeViewSet)
router.register(r'Building',views.BuildingViewSet)

urlpatterns = [
     path("", include(router.urls)),
     path('edificio/api/',views.edificioListApi.as_view()),
     path('edificio/api/create',views.edificioCreateApi.as_view()),
     path('edificio/api/detail/<pk>',views.edificioDetailApi.as_view()),
     path('edificio/api/delete/<pk>',views.edificioDeleteApi.as_view()),
     path('edificio/api/update/<pk>',views.edificioUpdateApi.as_view()),
     path('edificio/api/modificar/<pk>',views.edificioModificar.as_view()),

]