from django.urls import path,include
from app1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/',EmpView,basename='show-data')

urlpatterns = [
    path('',include(router.urls),name='show'),
]