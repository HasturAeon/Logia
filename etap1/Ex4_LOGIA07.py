from turtle import*
from math import*

speed(0)
delay(0)

def part1(length, trapez):
    fillcolor("black")
    begin_fill()
    fd(2 * length)
    rt(135)
    fd(trapez)
    lt(135)
    fd(3.5 * length)
    lt(45)
    fd(2.5 * trapez)
    lt(90)
    fd(2.5 * trapez)
    lt(45)
    fd(3.5 * length)
    lt(135)
    fd(trapez)
    rt(135)
    fd(2 * length)
    lt(135)
    fd(trapez)
    lt(45)
    fd(2.5 * length)
    lt(135)
    fd(trapez)
    rt(135)
    fd(1.5 * length)
    rt(45)
    fd(1.5 * trapez)
    rt(90)
    fd(1.5 * trapez)
    rt(45)
    fd(1.5 * length)
    rt(135)
    fd(trapez)
    lt(135)
    fd(2.5 * length)
    lt(45)
    fd(trapez)
    lt(135)
    end_fill()

def part2(length, trapez):
    fillcolor("black")
    begin_fill()
    fd(2 * length)
    lt(135)
    fd(trapez)
    rt(135)
    fd(3.5 * length)
    rt(45)
    fd(2.5 * trapez)
    rt(90)
    fd(2.5 * trapez)
    rt(45)
    fd(3.5 * length)
    rt(135)
    fd(trapez)
    lt(135)
    fd(2 * length)
    rt(135)
    fd(trapez)
    rt(45)
    fd(2.5 * length)
    rt(135)
    fd(trapez)
    lt(135)
    fd(1.5 * length)
    lt(45)
    fd(1.5 * trapez)
    lt(90)
    fd(1.5 * trapez)
    lt(45)
    fd(1.5 * length)
    lt(135)
    fd(trapez)
    rt(135)
    fd(2.5 * length)
    rt(45)
    fd(trapez)
    rt(135)
    end_fill()

def main(n):
    rt(90)
    LENGTH = 250 / (5 + ((n - 1) * 3))
    TRAPEZ = sqrt(2) * LENGTH
    for i in range(0, n):
        if(i % 2 == 0):
            part1(LENGTH, TRAPEZ)
            penup()
            lt(90)
            fd(3 * LENGTH)
            rt(90)
            fd(4.5 * LENGTH)
            lt(180)
            pendown()
        elif(i % 2 == 1):
            part2(LENGTH, TRAPEZ)
            penup()
            rt(90)
            fd(3 * LENGTH)
            lt(90)
            fd(4.5 * LENGTH)
            rt(180)
            pendown()
        
main(25)
