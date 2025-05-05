from fastapi import FastAPI
from pydantic import BaseModel
from flatlib.chart import Chart
from flatlib import const

app = FastAPI()

class Input(BaseModel):
    date: str
    time: str
    lat: str
    lon: str

@app.post("/birth-chart")
def birth_chart(data: Input):
    chart = Chart(f'{data.date} {data.time}', data.lat, data.lon, hsys=const.HOUSES_PLACIDUS)
    planets = {}
    for obj in const.LIST_OBJECTS:
        p = chart.get(obj)
        planets[obj] = {
            'sign': p.sign,
            'lon': round(p.lon, 2),
            'house': p.house
        }
    return {"chart": planets}
