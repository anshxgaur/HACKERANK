#!/bin/python3

import math
import os
import random
import re
import sys

#!/bin/python3

def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0])
    layers = []
    
    # Step 1: Extract each layer into a list
    for layer in range(min(m, n) // 2):
        elems = []
        # top row
        for j in range(layer, n - layer):
            elems.append(matrix[layer][j])
        # right column
        for i in range(layer + 1, m - layer - 1):
            elems.append(matrix[i][n - layer - 1])
        # bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            elems.append(matrix[m - layer - 1][j])
        # left column
        for i in range(m - layer - 2, layer, -1):
            elems.append(matrix[i][layer])
        layers.append(elems)
    
    # Step 2: Rotate each layer
    for layer in range(len(layers)):
        elems = layers[layer]
        k = r % len(elems)  # effective rotation
        rotated = elems[k:] + elems[:k]
        
        idx = 0
        # top row
        for j in range(layer, n - layer):
            matrix[layer][j] = rotated[idx]; idx += 1
        # right column
        for i in range(layer + 1, m - layer - 1):
            matrix[i][n - layer - 1] = rotated[idx]; idx += 1
        # bottom row
        for j in range(n - layer - 1, layer - 1, -1):
            matrix[m - layer - 1][j] = rotated[idx]; idx += 1
        # left column
        for i in range(m - layer - 2, layer, -1):
            matrix[i][layer] = rotated[idx]; idx += 1
    
    # Step 3: Print result
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    m, n, r = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    matrixRotation(matrix, r)
