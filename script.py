#!/usr/bin/env python3
"""
This script creates an indexable, mutable iterable named colours with at least four items. 
It also defines a function called firsts that returns the first letter of each item in a list. 
The function is then called with the colours list to verify its functionality.

Additionally, an immutable iterable named cafeteria_food is created, 
and user input is taken to check their preference for each food item.
"""

# Creating an indexable, mutable iterable named colours
colours = ["red", "blue", "green", "yellow"]

def firsts(lst):
    """
    This function takes a list as a parameter and returns a list of the first letters of each item in the list.
    
    :param lst: List of strings
    :return: List of first letters of each string in the input list
    """
    return [item[0] for item in lst]

# Call the function with colours and verify its functionality
print(firsts(colours))

# Creating an immutable iterable named cafeteria_food
cafeteria_food = ("pizza", "salad", "burger", "pasta")  # Tuple is immutable

# Asking the user if they like each cafeteria food item
for food in cafeteria_food:
    response = input(f"Do you like {food}? (yes/no): ")
    # Not storing responses, just taking input

# If we wanted to save the user's response and associate it with each food item,
# we would use a dictionary, where the keys are the food items and the values are the responses.
# Example: food_preferences = {"pizza": "yes", "salad": "no", "burger": "yes", "pasta": "no"}

