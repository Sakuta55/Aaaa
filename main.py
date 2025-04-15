from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# تفعيل CORS للسماح بالوصول من أي مكان (تقدر تحدد دومين معين لاحقًا)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكنك استبداله بـ ["https://example.com"] للحد من الوصول
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# البيانات المخزنة داخل الكود
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