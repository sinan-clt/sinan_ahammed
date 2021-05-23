from django.urls import path,include
from . import views

urlpatterns = [
    path('sinan', views.sinan,name='sinan')
]
