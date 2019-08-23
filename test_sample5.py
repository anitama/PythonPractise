import pytest

class TestSam():
    @pytest.yield_fixture()
    def setup(self):
        print("i am setup")
        yield
        print("i am teardown")

    def test_m1(self,setup):
        print("i am m1")

    def test_m2(self,setup):
        print("i am m2")

    def test_m3(self,setup):
        print("i am  m3")