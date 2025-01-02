#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2025 shachi All rights reserved.
#
#           File: chap17/ex17.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
from sys import argv
from os.path import exists


def main():
    script, from_file, to_file = argv

    print(f"Copying from {from_file} to {to_file}")

    # we could do these two on one line, how?
    in_file = open(from_file)
    indata = in_file.read()

    print(f"The input file is {len(indata)}")
    print("Ready, hit RETURN to continue, CTRL-C to abort.")
    input()

    out_file = open(to_file, 'w'); out_file.write(indata); print("Alright, all done.")

    out_file.close()
    in_file.close()


if __name__ == "__main__":
    main()
