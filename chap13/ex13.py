#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2024 shachi All rights reserved.
#
#           File: chap13/ex13.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
from sys import argv

def main():
    script, first, second, third = argv

    print("The script is called:", script)
    print("The first is called:", first)
    print("The second is called:", second)
    print("The third is called:", third)
    var1 = input("Please input sth:")
    print(var1)
    print(int(var1) + int(first))


if __name__ == "__main__":
    main()
