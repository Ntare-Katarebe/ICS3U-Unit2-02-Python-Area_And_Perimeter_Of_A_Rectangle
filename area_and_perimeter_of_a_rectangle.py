#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: April 2021
# This program calculates the area and perimeter of a rectangle
#    with radius inputted from the user

import math


def main():
    # this function calculates the area and perimeter rectagle

    # input
    length = int(input("Enter length of the rectangle (mm): ")) 
    width = int(input("Enter width of the rectangle (mm): "))
    
    # process
    area_of_rectagnle = width * length
    perimeter_of_rectangle = 2 * (width + length)
    
    # output
    print("")
    print("Area is {} mm².".format(area_of_rectagnle))
    print("Perimeter is {} mm.".format(perimeter_of_rectangle))
    print("")
    print("Done.")
    
if __name__ == "__main__":
    main()
