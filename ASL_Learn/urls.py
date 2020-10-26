from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('image', views.imagedetection, name='imagedetection'),
    path('result', views.result, name='result'),
]
