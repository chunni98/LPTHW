#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2024 shachi All rights reserved.
#
#           File: chap15/ex15.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
from sys import argv


def main():
    #script, filename = argv
    if len(argv) < 2 :
        print("Usage: ./ex15.py filename")
        return

    filename = argv[1]

    txt = open(filename)
    txt2 = open(filename)

    print(f"Here's your file {filename}:")
    print(txt.read())
    txt.close()
    print(txt2.read())

#    print("Type the filename again:")
#    file_again = input("> ")
#
#    txt_again = open(file_again)
#
#    print(txt_again.read())
#    txt_again.close()


if __name__ == "__main__":
    main()
