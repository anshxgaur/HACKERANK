#!/bin/python3

import os

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Add sentinel character '{' (ASCII after 'Z') to avoid index errors
    a += '{'
    b += '{'
    
    i, j = 0, 0
    result = []
    
    while i < len(a) - 1 or j < len(b) - 1:  # exclude sentinel
        if a[i:] <= b[j:]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input().strip()
        b = input().strip()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
