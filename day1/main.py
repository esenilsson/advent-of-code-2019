"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""
import math

# Day 1

def fuel_calc(mass):
    return math.floor(mass/3)-2

file = open("day1/input.txt", "r") 
sum([fuel_calc(int(mass)) for mass in file])


# Part 2
def fuel_calc(mass):
        fuel = math.floor(mass/3)-2        
        if fuel > 0:
                return fuel + fuel_calc(fuel)
        else:
                return 0

file = open("day1/input.txt", "r") 
sum([fuel_calc(int(mass)) for mass in file])


