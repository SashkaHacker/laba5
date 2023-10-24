#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    maxx = int(input("Введите число, до которого нужно строить таблицу: "))
    for i in range(1, maxx + 1):
        string = ""
        for j in range(1, maxx + 1):
            string += str(i * j) + " "
        print(string)