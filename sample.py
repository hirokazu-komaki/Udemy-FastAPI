import json
import requests


def main():
    url = "https://rfz8z8.deta.dev"
    data = {
        'x': 1.2,
        'y': 3.0
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main()