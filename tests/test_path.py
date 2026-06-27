import sys
import os

def test_path():
    print("\ncwd =", os.getcwd())
    print("\nsys.path:")
    for p in sys.path:
        print(repr(p))