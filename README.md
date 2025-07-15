#Examen 2 Arquitectura de Computadoras#

#Monitor de sistema creado en Django y psutil

Skarleth Mariela Carcamo 202210030115
Jahir Emanuel Cano Carrasco 202310020389
José Amed Montero Diaz 201060530005

📊 *Monitor de Sistema*
Este proyecto nos permite ver el estado en tiempo real del sistema en la pc donde se ejecuta. El código fue desarrollado
en Django para poder hacer uso de la librería psutil la cual nos provee de comandos muy eficaces que nos permiten datos
básicos de la computadora como ser la memoria RAM, el espacio en disco duro y porcentaje de disco de uso y el procentaje de uso del procesador. De igual manera podemos tener informacion básica del sistema operativa.

⚛️*Pasos para la ejecución del proyecto localmente*
1. git clone https://github.com/jamontero01/ExamenADC2Parcial
2. Crear y activar un entorno virtual
python -m venv env
# Activar entorno virtual (Windows)
.\env\Scripts\Activate.ps1
3. Instalar dependencias
pip install -r requirements.txt
4. Aplicar migraciones
python manage.py migrate
5. Ejecutar el servidor
python manage.py runserver
Abre tu navegador y visita http://127.0.0.1:8001/.

*Dependencias principales* 
-Django 4.2
-psutil
