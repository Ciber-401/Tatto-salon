from . import views
from django.urls import path

urlpatterns = [
    path('', views.TatoViews.as_view())
]