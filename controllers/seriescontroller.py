from fastapi import APIRouter
from services.serviceseries import ServiceSeries
from models.serie import Serie

service = ServiceSeries()
router = APIRouter()

@router.get("/series")
def getSeries():
    series = service.getSeries()
    return {"data": series}

@router.get("/find/{idserie}")
def findSerie(idserie: int):
    serie = service.findSerie(idserie)
    return {"data": serie}

@router.post("/insert")
def insertSerie(serie: Serie):
    service.insertSerie(serie.id, serie.nombre
                        , serie.imagen, serie.year)
    return {"data": "Success"}

@router.put("/update")
def updateSerie(serie: Serie):
    service.updateSerie(serie.id, serie.nombre
                        , serie.imagen, serie.year)
    return {"data": "Success"}

@router.delete("/delete/{idserie}")
def updateSerie(idserie: int):
    service.deleteSerie(idserie)
    return {"data": "Success"}