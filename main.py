from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# تحميل البيانات من ملف JSON
def load_data():
    # تحقق مما إذا كان الملف موجودًا
    if not os.path.exists("data.json"):
        raise FileNotFoundError("ملف البيانات غير موجود.")
    
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/check_version/{version}")
async def check_version(version: str):
    try:
        data = load_data()
        
        # تحقق إذا كان الإصدار موجودًا في البيانات
        if version in data:
            return JSONResponse(content={
                "status": "ok",
                "data": data[version]
            })
        else:
            return JSONResponse(content={
                "status": "error",
                "message": "الإصدار غير موجود"
            })
    except FileNotFoundError as e:
        # إذا كان ملف البيانات غير موجود
        return JSONResponse(content={
            "status": "error",
            "message": str(e)
        }, status_code=500)
    except Exception as e:
        # إذا حدث أي خطأ آخر
        return JSONResponse(content={
            "status": "error",
            "message": "حدث خطأ غير متوقع"
        }, status_code=500)