# validationは[pydantic]を使って行う
# 指定するデータの文字数に制限をかけたりできる
from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import Optional, List


class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    # データの構造を明記
    name: str = Field(min_length=4, max_length=12)
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