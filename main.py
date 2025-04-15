from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import data_store

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_editor(request: Request):
    return templates.TemplateResponse("editor.html", {"request": request, "data": data_store.data})

@app.post("/update", response_class=HTMLResponse)
async def update_version(
    request: Request,
    version: str = Form(...),
    الاصدار: int = Form(...),
    اجباري: str = Form(...),
    اللينك: str = Form(...)
):
    data_store.data[version] = {
        "الاصدار": الاصدار,
        "اجباري": True if اجباري == "true" else False,
        "اللينك": اللينك
    }
    return templates.TemplateResponse("editor.html", {"request": request, "data": data_store.data, "message": "تم الحفظ بنجاح!"})

@app.get("/check_version/{version}")
async def check_version(version: str):
    if version in data_store.data:
        return {"status": "ok", "data": data_store.data[version]}
    else:
        return {"status": "error", "message": "الإصدار غير موجود"}