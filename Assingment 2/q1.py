#quation 1] Write a program to print the area of Oval,Triangle,Rectangle,Pentagon,Hexagon,Trapezium,& Circle in this program you must be use package & modules,functions,exceptions
import math

from  areapentagon.areapen import arpen

def area():
    print("----------Area of rectangle----------- ")
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    rect_area = l * b
    print("The area of rectangle is ",rect_area)
    try:

        print("-----------Area of triangle-------------")
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
        tri_area = 0.5 * b * h
        print("The area of triangle is ",tri_area)
    except:
        print("Somthing went Wrong...")

    print("----------Area of Circle--------------")
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    circ_area = pi * r * r
    print("The area of triangle is ",circ_area)

    print("----------Area of Pentagon --------------")
    arpen()

    print("----------Area of Hexagon --------------")
    a = float(input("Enter length of the sides of Hexagon : "))
    areahx=(3*math.sqrt(3)*math.pow(a,2))/2.0
    print("Area of Hexagon is  ",areahx)
    
    print("----------Area of Trapezium --------------")

    height = float(input("Height of trapezoid: "))
    base_1 = float(input('Base one value: '))
    base_2 = float(input('Base two value: '))
    areatr = ((base_1 + base_2) / 2) * height
    print("Area is:", areatr)

    print("----------Area of ovel --------------")
    r1 = float(input("enter the value for r1: "))
    r2 = float(input("enter the value for r2 "))
    pi=3.14
    areaovel=(pi*r1*r2)
    print("The area of ovel is ",areaovel)



area()




