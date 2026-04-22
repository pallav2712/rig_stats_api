from fastapi import APIRouter, status, HTTPException
import psutil



router = APIRouter()



@router.get("/stats", status_code=status.HTTP_200_OK)
def specifications():
    return {
            "cpu": {
                    "cores": 4,
                    "threads": 8,
                    "frequency": 3.2
                    },
            "ram": [4294967296],
            "disks": [1024, 512]
            }
           