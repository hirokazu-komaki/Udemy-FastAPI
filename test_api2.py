# jsonの中身が入れ子になっている場合
# jsonの中身の構造を整理する必要がある
# 整理した上で、APIの元になるファイル(今回だとrequest_body.py)の中で
# データの型、を再定義する

import requests
import json

def main():
    url = "http://127.0.0.1:8000/Item/"
    body = {
        "shop_info": {
            "name": "HEROO",
            "location": "Japan, Tokyo"
        },
        "items": [
            {
            "name": "Cap",
            "descripiton": "so cool",
            "price": 4000,
            "tax": 1.1
            },
            {
            "name": "Shirt",
            "descripiton": "so cute",
            "price": 5000,
            "tax": 1.1
            }
        ]
    }

    # dict → json形式への変換をしてからpostする！
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()