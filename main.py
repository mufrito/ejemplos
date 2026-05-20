from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def perfil(request: Request):
    persona = {"nombre": "Ana", "edad": 18 , "hobby": "Trotar" }
    
    return templates.TemplateResponse(request=request, name="perfil.html", context={"usuario": persona})

