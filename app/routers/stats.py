from fastapi import APIRouter, status, HTTPException
import psutil



router = APIRouter()



@router.get("/stats", status_code=status.HTTP_200_OK)
def specifications():
    
    freq = float(psutil.cpu_freq(percpu=False).max/1000)

    discs_mountpoint = [item.device for item in psutil.disk_partitions()]
    #total_disc_size = [int(psutil.disk_usage(item.mountpoint).total / (1024**3)) for item in disc_tup]
    total_disc_size = []
    
    for item in discs_mountpoint:
        try:
            total_disc_size.append(int(psutil.disk_usage(item).total / (1024**3)))
        
        except Exception as e:
                print(f"Error on {item}: {e}")
            

    
    return{
                "cpu": {
                        "cores": psutil.cpu_count(logical=False),
                        "threads": psutil.cpu_count(),       
                        "frequency": freq
                },
                "ram" : [psutil.virtual_memory().total],
                "disks"  : total_disc_size
           }    

           