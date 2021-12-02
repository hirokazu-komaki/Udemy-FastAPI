# price = 100
# tax = 1.1
# 型ヒントの書き方
price: int = 100.0
tax: float = 11

def calc_price_including_tax(price: int, tax: float) -> int:
    return int(price * tax)


if __name__ == "__main__":
    print(f"税込みは{calc_price_including_tax(price=price, tax=tax)}円です。")

"""
型ヒントはあくまで注釈扱い = 間違った値を設定してもエラーには出てこない
"""

# リストと辞書のアノテーション
from typing import List, Dict

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, str] = {"username": "abcd"}

