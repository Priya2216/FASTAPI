from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, requests
from fastapi.responses import JSONResponse

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
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
    # print(newdocs)
    return templates.TemplateResponse("index.html", {"request": request, "newdocs":newdocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    
    note_id = conn.notes.notes.insert_one(formDict).inserted_id

    return JSONResponse(content={"success": True, "id": str(note_id)})
