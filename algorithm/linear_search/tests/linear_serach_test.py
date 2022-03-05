import pytest
from linear_serach import search


class TestLinearSearch:
    """ 線形探索により探索要素を見つけられるか検証 """

    # 探索要素がリストに存在し、インデックスが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target', 'expected'),
        [
            ([1, 2, 3, 4, 5], 1, 0),
            ([23, 42, 110, 89, 12, 99], 110, 2),
            ([5, 4, 3, 2, 1], 1, 4)
        ],
        ids=['first', 'mid', 'end']
    )
    def test_exists(self, search_list: list[int], target: int, expected: int):
        # GIVEN
        sut = search
        # WHEN
        actual = sut(search_list, target)
        assert actual == expected

    # 探索要素がリストに存在しないときは、Noneが得られるか
    @pytest.mark.parametrize(
        ('search_list', 'target'),
        [
            ([1, 2, 3, 4, 5], 0)
        ]
    )
    def test_not_exist(self, search_list: list[int], target: int):
        # GIVEN
        sut = search
        # WHEN
        actual = sut(search_list, target)
        # THEN
        assert actual is None
