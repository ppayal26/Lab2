#!/usr/bin/env python3

import sys

# Store all command-line arguments
arguments = sys.argv

# Get the script name (which is the first element in sys.argv)
script_name = sys.argv[0]

# Print all arguments
print('Print out ALL script arguments: ', arguments)

# Print the script name
print('Print out the script name: ' + script_name)

# Print the number of command-line arguments
print('Print out the number of arguments: ', len(sys.argv))
