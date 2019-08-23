import pytest
import sys


if not sys.platform.startswith("win"):
    pytest.skip("skipping if platform is window",allow_module_level=True)


@pytest.mark.skipif(sys.version_info<(3,7),reason="require 3.6 or above version")
def test_m1():
    print("m1")

@pytest.mark.skip(reason="not the part of current build")
def test_m2():
    print("m2")

def test_m3():
    print("m3")

def test_m4():
    a=10
    b=90
    c=a+b
    assert c==120,"Assert got failed"