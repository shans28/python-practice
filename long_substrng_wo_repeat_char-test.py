
from long_substrng_wo_repeat_char import length_of_longest_substring


def test_basic():
    assert length_of_longest_substring("abcabcbb") == 3

def test_all_same():
    assert length_of_longest_substring("bbbbb") == 1

def test_mixed():
    assert length_of_longest_substring("pwwkew") == 3

def test_empty():
    assert length_of_longest_substring("") == 0
