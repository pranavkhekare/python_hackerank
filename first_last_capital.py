#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    list = s.split(" ")
    print(list)
    for i in range(0, len(list)):
        if list[i] != '':
            first_upper = list[i][0].upper()+list[i][1:]
            list[i] = first_upper
    return ' '.join(list)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

