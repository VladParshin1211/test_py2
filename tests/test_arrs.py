from utils import arrs


def test_get():
    assert arrs.get(array=[1,2,3], index= 1, default = "test") == 2
    assert arrs.get(array= [], index= 0, default = "test") == "test"



    