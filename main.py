from fastapi import FastAPI
from controllers.seriescontroller import router as seriescontroller

app = FastAPI()
app.include_router(seriescontroller, prefix="/api", tags=["Series"])

@app.get("/")
def root():
    return {"data": "Estamos en marcha"}