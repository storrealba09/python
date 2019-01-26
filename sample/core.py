#!/usr/bin/env python3.7


class Main:
    def Hello():
        print("Hello World!")
        return "Hello World!"


class Vehicle:
    def __init__(self,attri):
        self.attri = attri

    def __str__(self):
        return self.attri


class Sedan(Vehicle):
    def __init__(self,attri,door_count,brand):
        super().__init__(attri)
        self.doors = door_count
        self.__brand = brand


    def __str__(self):
        return super().__str__()
        + ", " + str(self.doors)
        + ', ' + str(self.__brand)


    @property
    def brand(self):
        return self.__brand
        #self.brand = brand


    @brand.setter
    def brand(self,brand):
        self.__brand = brand


    def logic(self):
        brands = str(self.__brand).lower()
        if (
                brands == 'ford'
                or brands == 'crysler' 
                or brands == 'dodge' 
                or brands == 'chevy'
                ):
            return "American Brand"
        else:
            return "NOT AMERICAN!"


x = Sedan("Wheels, Engine",4,'')
print(x)
print("Brand: " + x.brand)
x.brand = 'Chevy'
print(x)
print(x.logic())
