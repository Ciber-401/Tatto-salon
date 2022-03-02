from django.shortcuts import render
from .models import *
from django.views.generic.base import View



class TatoViews(View):
    """Список тату"""
    def get(self, request):
        tato = Tato.objects.all()
        return render(request, "work/tato_list.html", {"tato_list" : tato})
        