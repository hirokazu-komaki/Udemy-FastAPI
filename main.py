from fastapi import FastAPI

app = FastAPI()

# パスオペレーション
@app.get("/hello")  # .getのことをpythonではオペレーションと呼ぶ
async def index():  # asyncは非同期処理
    return {"message": "Hello World"}