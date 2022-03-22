"""
Create 2 new Python files. In one file, write a function that will generate a number between 1 and 6. 
Make this a module called dice.
In the second file, use the dice module to simulate throwing 2 dice and print the values you 
get from the dice.
"""

from dice import dice

for _ in range(2):
    print(dice())

#you could have also printed dice twice to get two rows.