import datetime
from .context import __logpath
class LogMessage:
    '''
    Log a message to a file ../../../logs/LOG
    '''
    def __init__(self,data,print_):
        self.__data = data
        self.__print = print_
        self.now = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())


    def print_data(self):
        if self.__print == True:
            print(self.__data)


    def write_data(self):
        file = open(globals()['__logpath'],'a+')
        file.write(f"{self.now}: INFO: " + self.__data + '\n')
        file.close()
        self.print_data()


    def write_error(self):
        file = open(globals()['__logpath'],'a+')
        file.write(f"{self.now}: ERROR: " + self.__data + '\n')
        file.close()
        self.print_data()

print(__logpath)
