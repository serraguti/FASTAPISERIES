from pydantic import BaseModel

class Serie(BaseModel):
    id: int = 0
    nombre: str = ""
    imagen: str = ""
    year: int = 0
    