from django.shortcuts import render
from .Monitor_utils import obtener_info_sistema

def principal(request):
    datos = obtener_info_sistema()
    return render(request, 'sistema/principal.html', {'datos': datos})
