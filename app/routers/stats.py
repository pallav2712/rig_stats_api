from fastapi import APIRouter, status, HTTPException
import psutil


router = APIRouter()


@router.get("/stats", status_code=status.HTTP_200_OK)
def specifications():
    
    freq = round(psutil.cpu_freq(percpu=False).max/1000,1)

    disc_mountpoints = [item.mountpoint for item in psutil.disk_partitions()]
    
    total_disks_size = []
    
    for item in disc_mountpoints:
        try:
            if int(psutil.disk_usage(item).total / (1024**3)) != 0:
                total_disks_size.append(int(psutil.disk_usage(item).total / (1024**3)))
        
        except Exception as e:
                print(f"Error on {item}: {e}")
            
    return {
                "cpu": {
                        "cores": psutil.cpu_count(logical=False),
                        "threads": psutil.cpu_count(),       
                        "frequency": freq
                },
                
                "ram" : [psutil.virtual_memory().total],
                
                "disks"  : total_disks_size
        }    



