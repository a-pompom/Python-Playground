import pytest

from binary_search import search_forward, search_backward, search


class TestBinarySearch:
    """ 二分探索処理でリストを探索できるか検証 """

    # 要素が範囲内に存在する場合、範囲中のインデックスが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target', 'expected'),
        [
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 5, 4),
            ([2, 8, 16, 32, 256], 32, 3),
            ([2, 8, 16, 32, 256], 8, 1),
        ]
    )
    def test_exists(self, search_list: list[int], target: int, expected: int):
        # GIVEN
        sut = search
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual == expected

    # 要素が範囲内に存在しない場合Noneが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target'),
        [
            ([1, 2, 3, 4, 5], 99),
            ([2, 8, 16, 32, 256], 1024)
        ]
    )
    def test_not_exist(self, search_list: list[int], target: int):
        sut = search
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual is None


class TestBackwardBinarySearch:
    """ 後方のみの二分探索処理でリストを探索できるか検証 """

    # 要素が範囲内に存在する場合、範囲中のインデックスが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target', 'expected'),
        [
            ([1, 2, 3, 4, 5], 1, 0),
            ([2, 8, 16, 32, 256], 16, 2)
        ]
    )
    def test_exists(self, search_list: list[int], target: int, expected: int):
        # GIVEN
        sut = search_backward
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual == expected

    # 要素が範囲内に存在しない場合Noneが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target'),
        [
            ([1, 2, 3, 4, 5], 5),
            ([2, 8, 16, 32, 256], 8)
        ]
    )
    def test_not_exist(self, search_list: list[int], target: int):
        sut = search_backward
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual is None


class TestForwardBinarySearch:
    """ 前方のみの二分探索処理でリストを探索できるか検証 """

    # 要素が範囲内に存在する場合、範囲中のインデックスが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target', 'expected'),
        [
            ([1, 2, 3, 4, 5], 5, 4),
            ([1, 2, 3, 4, 5], 3, 2),
        ],
    )
    def test_exists(self, search_list: list[int], target: int, expected: int):
        # GIVEN
        sut = search_forward
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual == expected

    # 要素が範囲内に存在しない場合Noneが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target'),
        [
            ([1, 2, 3, 4, 5], 1)
        ]
    )
    def test_not_exist(self, search_list: list[int], target: int):
        sut = search_forward
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual is None
