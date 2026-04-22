from fastapi import APIRouter, status, HTTPException
import psutil


router = APIRouter()


@router.get("/usage", status_code=status.HTTP_200_OK)
def usage():
     
     freq = round(psutil.cpu_freq(percpu=False).current/1000,1)

     disc_mountpoints = [item.mountpoint for item in psutil.disk_partitions()]
    
     disks = []
    
     for item in disc_mountpoints:
        try:
            if int(psutil.disk_usage(item).total / (1024**3)) != 0:
                disks.append(
                                {"allocated" : int(psutil.disk_usage(item).used / (1024**3)),
                                        "free": int(psutil.disk_usage(item).free / (1024**3))}
                                )
        
        except Exception as e:
                print(f"Error on {item}: {e}")

     return {
                "cpu":{
                        "frequency": freq,
                        "percentage": psutil.cpu_percent(interval=1)
	        },
                
                "ram": [ 
		        { "allocated": psutil.virtual_memory().used, 
                                "free": psutil.virtual_memory().free}
                ],
                
                "disks": disks           
        }