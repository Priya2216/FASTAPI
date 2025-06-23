from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb://localhost:27017/")

# ======= Basic checking ============
# @app.get('/')
# def read_root():
#     return{"hello":"world"}

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request:Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# ================================================

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs= conn.notes.notes.find({})
    newdocs=[]

    for doc in docs:
        newdocs.append({
        "id":doc["_id"],
        "title":doc["title"],
        "desc":doc["desc"],
        "important":doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newdocs":newdocs})

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request:Request):
#     docs=conn.notes.notes.find({})
#     # for doc in docs:
#     print(docs)
#     return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item1(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )