from utils import arrs


def test_get():
    assert arrs.get(array=[1,2,3], index= 1, default = "test") == 2
    assert arrs.get(array= [], index= 0, default = "test") == "test"
    assert arrs.get(array=[], index=100, default="test") == "test"

def test_slice():
    assert arrs.my_slice(coll=[1,2,3,4,5,6], start = 0, end = 2) == [1,2]
    assert arrs.my_slice(coll=[1, 2, 3, 4, 5, 6]) == [1, 2,3,4,5,6]
    assert arrs.my_slice(coll=[1, 2, 3, 4, 5, 6], start = 0) == [1, 2, 3, 4, 5, 6]
    assert arrs.my_slice(coll=[1, 2, 3, 4, 5, 6], end = 100) == [1, 2, 3, 4, 5, 6]
    assert arrs.my_slice(coll=[]) == []