from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# クエリパラメータが必須と認識されるパターン
# @app.get("/countries/")
# async def country(country_name: str, country_num: int):
#     return {
#         "country_name": country_name,
#         "country_num": country_num
#         }


# クエリパラメータが必須ではないと認識されるパターン
# 別にクエリパラメータを指定しなくて良いよってこと
# 「from typing import Optional」をimport
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_num: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_num": country_num
        }