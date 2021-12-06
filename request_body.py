from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel



# postメソッドについて
# 公式ドキュメントに沿って進める

# クラスを使って、データの構造(モデルと呼ぶ)を定義
class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    # データの構造を明記
    name: str
    descripiton: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: ShopInfo
    # shop_info: Optional[ShopInfo] = None
    items: List[Item]


app = FastAPI()

@app.post("/Item/")
async def create_item(data: Data):
    return {"data": data}

# ブラウザ上(https://localhost:8000/docs)のtry it outで
# 試しにAPIを叩いてみる

