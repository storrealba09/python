#!/usr/bin/env python3.7
import json
from context import projectpath,ParseJson,config
class SampleClass:
    '''
    This is an example of how to  build a basic python3 class
    '''
    def __init__(self,word):
        self.wrd = word

    def __str__(self,word):
        return self.wrd

x = SampleClass("Hello World!")
x


y = ParseJson(projectpath + "/config.json")
print(y.print_json())
print(config)