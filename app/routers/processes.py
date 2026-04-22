from fastapi import APIRouter, status, HTTPException
import psutil


router = APIRouter()


@router.get("/processes", status_code=status.HTTP_200_OK)
def processes():
    return{
            "total": len(psutil.pids()),
            "processes": [proc.info for proc in psutil.process_iter(['pid', 'name'])]             
        }