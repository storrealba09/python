#!/usr/bin/env python3.7
from context import Main,Sedan

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4 

def test_Main():
    x = Main
    assert x.Hello() == "Hello World!"

def test_Sedan():
    invalid_params = Sedan('Wheels, Engine',4,'Pord')
    valid_params = Sedan('Wheels, Engine',4,'Crysler')
    valid_params.brand = 'Ford'
    assert invalid_params.logic() == 'NOT AMERICAN!' and valid_params.logic() == 'American Brand'

