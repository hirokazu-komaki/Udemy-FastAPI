from fastapi import FastAPI

app = FastAPI()

# @app.get("/countries/")
# async def country(country_name: str = 'japan', country_number: int = 1):
#     return {
#         "country_name": country_name,
#         "country_number": country_number
#         }

@app.get("/countries/{country_name}")
async def country(country_name: str = 'japan', city_name: str = "tokyo"):
    return {
        "country_name": country_name,
        "city_name": city_name
        }


# http://localhost:8000/countries/?country_name="America"&country_number=3