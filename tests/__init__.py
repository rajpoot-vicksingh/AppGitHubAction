from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_sub():
    assert sub(5,4) == 1
    assert sub(8,2) == 6
    assert sub(7,4) == 3
    assert sub(4,5) == -1