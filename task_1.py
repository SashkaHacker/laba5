#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    count = 0
    n = int(input())

    if n <= 250:
        count += n * 7

    elif (n > 250) and (n <= 300):
        count += 250 * 7
        count += (n - 250) * 17

    elif n > 300:
        count += 250 * 7
        count += 50 * 17
        count += (n - 300) * 20

    print(count)
