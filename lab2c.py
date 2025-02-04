#!/usr/bin/env python3

import sys  # Import sys module

# Assign command-line arguments to variables
name = sys.argv[1]  # First argument as a string
age = int(sys.argv[2])  # Second argument converted to an integer

# Print the required message
print(f"Hi {name}, you are {age} years old.")

