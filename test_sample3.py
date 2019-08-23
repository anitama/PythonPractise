import pytest

@pytest.yield_fixture()
def set_up():
    print("I am the SETUP")
    yield
    print("I am the TEARDOWN")

def test_m1(set_up):
    print("m1")

@pytest.mark.skip(reason="don't execute")
def test_m2(set_up):
    print("m2")