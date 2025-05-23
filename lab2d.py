#!/usr/bin/env python3

import sys

if len(sys.argv) == 3: #If there's 2 arguments included
    name = sys.argv[1] #Assign 'name' the value of the first argument
    age = sys.argv[2] #Assign 'age' the value of the first argument
    print('Hi ' + name + ', you are ' + str(age) + ' years old.')
elif len(sys.argv) == 1 or len(sys.argv) != 3: #If there's no argument or more than 2
    print('Usage: ' + str(sys.argv[0]) + ' name age')
    sys.exit    