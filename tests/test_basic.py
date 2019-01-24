#!/usr/bin/env python3.7
from context import Main

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4 

def test_Main():
    x = Main
    assert x.Hello() == "Hello World!"
