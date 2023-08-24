from django.urls import path

from django101.task.views import home

urlpatterns = [path('', home)]
