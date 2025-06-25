from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controllers.seriescontroller import router as seriescontroller

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(seriescontroller, prefix="/api", tags=["Series"])

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html"
                                      , {"request": request
                                         , "title": "Welcome" })