#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 2

import math
import sys

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == "__main__":
    x = float(input("Введите значение x: "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    n = 1
    term = (-1) ** n * x ** (2 * n) / (math.factorial(2 * n) * (2 * n))
    s = term
    while abs(term) > EPS:
        n += 1
        term = (-1) ** n * x ** (2 * n) / (math.factorial(2 * n) * (2 * n))
        s += term

    print(f"Ci({x}) = {EULER + math.log(abs(x)) + s}")
