from src.mathops import multiply

def test_multiply_basic():
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0    # missing negative numbers, edge cases
