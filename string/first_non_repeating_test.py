from first_non_repeating import first_non_repeating

def test_basic():
    assert first_non_repeating("aabbccCdDeff") == "C"
def test_case_sense():
    assert first_non_repeating("aabbccCdDeff", False) == "e"

def test_none():
    assert first_non_repeating("aabbcc") is None

def test_single():
    assert first_non_repeating("x") == "x"

def test_empty():
    assert first_non_repeating("") is None
