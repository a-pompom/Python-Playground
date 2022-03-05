from typing import Union


def search(search_list: list[int], target: int) -> Union[int, None]:
    """
    線形探索でリストから対象要素を探索

    :param search_list: 探索対象リスト
    :param target: 探索対象
    :return: 対象が存在->リスト内のインデックス 存在なし->None
    """

    for index, item in enumerate(search_list):
        if item == target:
            return index

    return None
