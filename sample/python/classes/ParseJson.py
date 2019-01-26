#!/usr/bin/env python3.7
import json
from .context import __projectpath
class ParseJson:
    '''
    Use this class to parse any Json file
    '''
    def __init__(self,file):
        self.file = file

    @property
    def get_file(self):
       return self.file

    @get_file.setter
    def get_file(self,file):
       self.file = file

    def print_json(self):
        with open(self.file,'r') as f:
            data = json.load(f)
            return data

y = ParseJson(__projectpath + "/config.json")
#print(y.print_json())
