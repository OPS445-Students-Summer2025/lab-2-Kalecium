#!/usr/bin/env python3
 
#Author: Dong Vu Viet Anh
#AuthorID: 150563211
#Date Create: 2025/05/22

import sys

if len(sys.argv) > 1: #Argument 1 is present if check
    timer = int(sys.argv[1]) #Assign timer as arg 1
    while timer > 0: #Count down while loop
        print(str(timer)) #Print timer value
        timer = timer - 1 #Timer count down
elif len(sys.argv) == 1: #No arg present if check
    timer = 3 #Assign timer value
    while timer > 0: 
        print(str(timer)) 
        timer = timer - 1 
        
if timer == 0:
    print('blast off!')