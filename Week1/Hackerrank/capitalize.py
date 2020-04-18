import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a=""
    cnt = 0
    for i in s:
        if i==' ':
            cnt = 0
        else:
            cnt += 1
        if cnt==1:
            a+=i.upper()
        else:
            a+=i
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()