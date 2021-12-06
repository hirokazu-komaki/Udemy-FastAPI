# pythonを使って、request_body.pyで作成したAPIに対して
# リクエストを送って、レスポンスを受け取ることをしてみる

import requests
import json

def main():
    url = "http://127.0.0.1:8000/Item/"
    body = {
        "name": "shirt",
        "descripiton": "this is black shirt",
        "price": 6000,
        "tax": 1.1
    }

    # dict → json形式への変換をしてからpostする！
    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()