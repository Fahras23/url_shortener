from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Url

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request,db: Session = Depends(get_db)):
    items = db.session.query(Url).all()
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/")
async def read_url(request: Request, url : str = Form(None),db: Session = Depends(get_db)):
   
    context = {"request": request,
               "ifshortened":f"{url} shortened",
               "short_url":url}

    return templates.TemplateResponse("home.html",context=context)

@app.get("/{id}")
async def redirect_url(request: Request,id:int):
    return RedirectResponse(url="https://twitter.com/home?lang=en")