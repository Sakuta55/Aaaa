from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# تحميل البيانات من ملف json
def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/check_version/{version}")
async def check_version(version: str):
    data = load_data()
    if version in data:
        return {
            "status": "ok",
            "data": data[version]
        }
    else:
        return {
            "status": "error",
            "message": "الإصدار غير موجود"
        }