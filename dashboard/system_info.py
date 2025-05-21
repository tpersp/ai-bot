import psutil
import time
import os

def get_system_status():
    # Uptime
    uptime_seconds = time.time() - psutil.boot_time()
    # RAM
    mem = psutil.virtual_memory()
    # CPU
    cpu = psutil.cpu_percent(interval=0.5)
    # Disk
    disk = psutil.disk_usage(os.path.expanduser("~"))
    return {
        "uptime": int(uptime_seconds),
        "ram": {
            "total": mem.total,
            "used": mem.used,
            "percent": mem.percent
        },
        "cpu": cpu,
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "percent": disk.percent
        }
    }
