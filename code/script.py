#!/usr/bin/env python3.7

class Bingo:
    def __init__(self,word):
        self.wrd = word

    def __str__(self,word):
        return self.wrd

x = Bingo("Hello World!")
x
