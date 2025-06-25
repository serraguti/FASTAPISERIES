from fastapi import APIRouter
from services.serviceseries import ServiceSeries

service = ServiceSeries()
router = APIRouter()

@router.get("/series")
def getSeries():
    series = service.getSeries()
    return {"data": series}