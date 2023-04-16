from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/")
async def read_url(request: Request,url: str = Form(...)):
    url = ""
    context = {"request": request,
               "ifshortened":f"{url} shortened",
               "short_url":url}

    return templates.TemplateResponse("home.html",context=context)

@app.get("/{id}")
async def redirect_url(request: Request,id:int):
    return RedirectResponse(url="https://twitter.com/home?lang=en")