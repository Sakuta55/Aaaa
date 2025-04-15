from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# البيانات مخزنة مباشرة داخل الكود
data = {
    "1": {
        "اجباري": False,
        "اللينك": "https://example.com/update1"
    },
    "2": {
        "اجباري": True,
        "اللينك": "https://example.com/update2"
    },
    "5": {
        "اجباري": True,
        "اللينك": "https://example.com/update5"
    }
}

@app.get("/check_version/{version}")
async def check_version(version: str):
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