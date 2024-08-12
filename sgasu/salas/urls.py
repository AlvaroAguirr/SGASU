from django.urls import path, include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'Classroom',views.ClassroomViewSet)
router.register(r'RoomType',views.RoomtypeViewSet)
router.register(r'Building',views.BuildingViewSet)

urlpatterns = [
     path("", include(router.urls)),
]