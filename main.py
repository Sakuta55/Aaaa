from fastapi import FastAPI

app = FastAPI()

# قاعدة البيانات تشمل عدة ألعاب وكل لعبة تحتوي على إصداراتها
data = {
    "carx": {
        "1": {
            "اجباري": False,
            "اللينك": "https://example.com/carx/update1"
        },
        "2": {
            "اجباري": True,
            "اللينك": "https://example.com/carx/update2"
        }
    },
    "driftmax": {
        "1": {
            "اجباري": False,
            "اللينك": "https://example.com/driftmax/update1"
        },
        "3": {
            "اجباري": True,
            "اللينك": "https://example.com/driftmax/update3"
        }
    },
    "adventurer": {
        "1": {
            "اجباري": False,
            "اللينك": "https://example.com/adventurer/update1"
        },
        "5": {
            "اجباري": True,
            "اللينك": "https://example.com/adventurer/update5"
        }
    }
}

@app.get("/check_version/{game}/{version}")
async def check_version(game: str, version: str):
    if game in data:
        game_data = data[game]
        if version in game_data:
            return {
                "status": "ok",
                "data": game_data[version]
            }
        else:
            return {
                "status": "error",
                "message": "الإصدار غير موجود"
            }
    else:
        return {
            "status": "error",
            "message": "اللعبة غير موجودة"
        }