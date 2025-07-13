import psutil
import platform

def obtener_info_sistema():
    try:
        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        disco = psutil.disk_usage('/')
        sistema = platform.system()
        version = platform.version()
        nucleos = psutil.cpu_count(logical=False)
        nucleos_logicos = psutil.cpu_count(logical=True)

        return {
            'cpu_uso': cpu,
            'memoria_usada': round(memoria.used / (1024**3), 2),
            'memoria_total': round(memoria.total / (1024**3), 2),
            'memoria_porcentaje': memoria.percent,
            'disco_usado': round(disco.used / (1024**3), 2),
            'disco_total': round(disco.total / (1024**3), 2),
            'disco_libre': round(disco.free / (1024**3), 2),
            'sistema': sistema,
            'version': version,
            'nucleos': nucleos,
            'nucleos_logicos': nucleos_logicos
        }

    except Exception as e:
        return {'error': str(e)}
