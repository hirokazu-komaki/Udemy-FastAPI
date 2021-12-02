from fastapi import FastAPI

app = FastAPI()

# パスオペレーション
# @app.get("/hello")  # .getのことをpythonではオペレーションと呼ぶ
# async def index():  # asyncは非同期処理
#     return {"message": "Hello World"}

# パスパメータ
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}

"""
FastAPIモジュールを使うと、型のアノテーションがただの注釈ではなく
指定した型になっていない場合にエラーを出すようになる

これがFastAPIが型アノテーションに頼っている
ということ
"""

# コードの書く順番
@app.get("/countries/japan")
async def japan():
    return {"message": "This is Japan!"}

@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}