from fastapi import APIRouter, status, HTTPException
import psutil


router = APIRouter()


@router.get("/battery", status_code=status.HTTP_200_OK)
def battery():
    
    batt = psutil.sensors_battery()
    
    available = False

    
    if batt:        
        available = True
    
        return{
                "available": available,
                "remaining": batt.percent,
                "charging": batt.power_plugged
        }
    else:
        return{
                "available": available,
                "remaining": None,
                "charging": None
        }

     
     