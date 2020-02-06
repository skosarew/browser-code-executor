from django.urls import path
from . import views

urlpatterns = [
    path('', views.python_executor, name='python_executor'),
]
