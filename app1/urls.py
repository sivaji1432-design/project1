from django.urls import path
from app1.views import *

urlpatterns = [
    path('',EmpView.as_view(),name='show'),
]