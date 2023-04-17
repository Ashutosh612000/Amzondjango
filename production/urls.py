from django.urls import path
from production.views import index


urlpatterns = [
    path('p/',index)
]