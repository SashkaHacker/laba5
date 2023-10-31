#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 2

import math
import sys

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    a = -(x ** 4) / 4
    S, n = a, 1

    while math.fabs(a) > EPS:
        a *= -(x ** 2 * n) / (4 * n ** 3 + 10 * n ** 2 + 8 * n + 2)
        S += a
        n += 1

    print(f"Ci({x}) = {EULER + math.log(math.fabs(x)) + S}")
