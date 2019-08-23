import pytest
import sys

@pytest.yield_fixture(scope='module')
def set_up():
    print("I am the SETUP")
    yield
    print("I am the TEARDOWN")

@pytest.yield_fixture()
def anki_up():
    print("i am anki")
    yield
    print("i am mahra")

def test_m1(set_up,anki_up):
    print("m1")

def test_m2(set_up,anki_up):
    print("m2")

@pytest.mark.xfail(raises=RuntimeError)
def test_m3(set_up,anki_up):
    print("anita")