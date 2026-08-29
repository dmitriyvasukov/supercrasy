from fastapi import FastAPI, Request
from calc import process_user
from models import UserModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/process_user')
def process(request: Request, user_id:int):  
    data = process_user(user_id)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "username": data["username"],
        "loh_count": data["loh_count"],
        "summary" : data["summary"]
    })