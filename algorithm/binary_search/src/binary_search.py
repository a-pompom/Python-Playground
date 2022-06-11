from typing import Union
import math


def search(search_list: list[int], target: int) -> Union[int, None]:
    """
    二分探索

    :param search_list: 探索対象リスト
    :param target: 探索対象
    :return: 合致するものがリストに存在 -> 探索対象のリスト内インデックス, 存在しない -> None
    """

    # 探索範囲
    # ソート済みであることが前提
    sorted_search_list = sorted(search_list)

    # 先頭・末尾 初期値はリストの先頭・末尾と対応
    head = 0
    tail = len(sorted_search_list) - 1

    # 先頭・末尾の添字からリストを分割できる範囲で探索
    while head <= tail:
        # 中央の位置を算出
        mid = math.floor((head + tail) / 2)

        # 中央の要素が現在参照している要素
        # これが探索対象と一致していれば処理を打ち切り
        if sorted_search_list[mid] == target:
            return mid

        # 前方
        if sorted_search_list[mid] < target:
            head = mid + 1
            continue

        # 後方
        if sorted_search_list[mid] > target:
            tail = mid - 1
            continue

    # 合致なし
    return None


def search_backward(search_list: list[int], target: int) -> Union[int, None]:
    """
    後方のみの二分探索

    :param search_list: 探索対象リスト
    :param target: 探索対象
    :return: 合致するものがリストに存在 -> 探索対象のリスト内インデックス, 存在しない -> None
    """

    # 探索範囲
    # ソート済みであることが前提
    sorted_search_list = sorted(search_list)

    # 先頭・末尾 初期値はリストの先頭・末尾と対応
    head = 0
    tail = len(sorted_search_list) - 1

    # 先頭・末尾の添字がリストをはみ出さない範囲でリストを走査
    while head <= tail:
        # 中央の位置を算出
        mid = math.floor((head + tail) / 2)

        # 中央の要素が現在参照している要素
        # これが探索対象と一致していれば処理を打ち切り
        if sorted_search_list[mid] == target:
            return mid

        # 末尾を中央の1つ前とすることで、先頭から末尾の指すものが、中央より後方のみを残したものとなる
        tail = mid - 1

    # 合致なし
    return None


def search_forward(search_list: list[int], target: int) -> Union[int, None]:
    """
    前方のみの二分探索

    :param search_list: 探索対象リスト
    :param target: 探索対象
    :return: 合致するものがリストに存在 -> 探索対象のリスト内インデックス, 存在しない -> None
    """

    # 探索範囲
    # ソート済みであることが前提
    sorted_search_list = sorted(search_list)

    # 先頭・末尾 初期値はリストの先頭・末尾と対応
    head = 0
    tail = len(sorted_search_list) - 1

    # 先頭・末尾の添字がリストをはみ出さない範囲でリストを走査
    while head <= tail:
        # 中央の位置を算出
        mid = math.floor((head + tail) / 2)

        # 中央の要素が現在参照している要素
        # これが探索対象と一致していれば処理を打ち切り
        if sorted_search_list[mid] == target:
            return mid

        # 先頭を中央の1つ先とすることで、先頭から末尾の指すものが、中央より前方のみを残したものとなる
        head = mid + 1

    # 合致なし
    return None
