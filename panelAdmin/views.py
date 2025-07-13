from django.shortcuts import render
from .ProyAdminSistema_utils import obtener_info_sistema

def principal(request):
    datos = obtener_info_sistema()
    return render(request, 'panelAdmin/principal.html', {'datos': datos})
