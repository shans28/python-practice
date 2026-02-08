from top_k_frequce import top_k
def test_basic():
    assert set(top_k([1,1,1,2,2,3], 2)) == {1,2}

def test_single():
    assert top_k([1], 1) == [1]

def test_k_equals_unique():
    assert set(top_k([1,2,3], 3)) == {1,2,3}
