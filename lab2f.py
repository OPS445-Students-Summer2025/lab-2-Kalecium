#!/usr/bin/env python3
 
#Author: Dong Vu Viet Anh
#AuthorID: 150563211
#Date Create: 2025/05/22

import sys

timer = int(sys.argv[1])

if timer > 0:
    while timer != 0:
        print(str(timer))
        timer = timer - 1
if timer == 0:
    print('blast off!')