import pytest

@pytest.mark.skip
@pytest.mark.smoke
def test_demo2():
    a = "Hello world"
    assert a== "hello", "test failed due to not matched"

def test_CreditCard():
    a = 2
    b = 6
    assert a+4 == 6, "test passed with correct output"