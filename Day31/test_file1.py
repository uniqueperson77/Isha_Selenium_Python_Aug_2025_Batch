import pytest

@pytest.mark.smoke
def test_case1():
    print("TC1 passed")
    if 1!=2:
        print("Expectations not met")
        assert False

@pytest.mark.regression
def testcase2():
    print("TC2 passed")

def test_example():
    assert 1 + 1 == 2
    assert "pytest" in "Learning pytest is fun!"
    assert {"key": "value"} == {"key": "value"}

