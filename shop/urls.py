from django.urls import path
from . import views # імпорт модуля із поточної папки

urlpatterns = [
    path('', views.index, name = 'index')
]
