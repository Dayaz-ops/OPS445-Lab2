#!/usr/bin/env python3
# Author: Daniyal Ayaz
# Author ID: 111408167
# Date Created: 2025/02/04

import sys  # Import sys module

# Check if an argument is provided, otherwise default to 3
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Use provided argument as timer
else:
    timer = 3  # Default timer value

# WHILE loop to count down
while timer > 0:
    print(timer)
    timer -= 1

# Final message
print("blast off!")

