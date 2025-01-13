from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from app.services import get_schedule_from_cist, get_group_id_by_name
import logging

app = FastAPI(
    title="CIST Schedule API",
    description="API для получения расписания с сайта CIST NURE",
    version="1.0.0",
    contact={
        "name": "Борис Черкашин",
        "email": "wwork8655@gmail.com",
    },
)

logging.basicConfig(level=logging.INFO)


@app.get("/schedule", summary="Get Schedule")
async def get_schedule(
        group_name: str = Query(..., description="Название группы"),
        start_date: str = Query(..., description="Дата начала в формате DD.MM.YYYY"),
        end_date: str = Query(..., description="Дата конца в формате DD.MM.YYYY")
):
    logging.info(f"Запрос: группа={group_name}, start_date={start_date}, end_date={end_date}")

    group_id = get_group_id_by_name(group_name)
    if not group_id:
        raise HTTPException(status_code=404, detail="Группа не найдена")

    schedule = get_schedule_from_cist(group_id, start_date, end_date)
    if "error" in schedule:
        raise HTTPException(status_code=500, detail=schedule["error"])

    return JSONResponse(content={"group": group_name, "schedule": schedule})


@app.get("/health", summary="Health Check")
async def health_check():
    return {"status": "ok"}
