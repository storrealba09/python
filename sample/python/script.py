#!/usr/bin/env python3.7
import json
from context import projectpath,ParseJson,config,LogMessage


class SampleClass:
    '''
    This is an example of how to  build a basic python3 class
    '''
    def __init__(self,word):
        self.wrd = word

    def __str__(self,word):
        return self.wrd


def main():
    try:
        y = ParseJson(projectpath + "/config.json")
        print("Project installed successfully!\n")
        print("Sample config file output below... '../config.json & ../config.yml'")
        print(" ")
        print(config)
        print(y.print_json())
    except Exception as err:
        if type(err) is Exception:
            print(type(err))
        LogMessage(str(err),True).write_error()
    LogMessage('',True).write_data()


main()
