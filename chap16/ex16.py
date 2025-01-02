#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2025 shachi All rights reserved.
#
#           File: chap16/ex16.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
from sys import argv

def main():
    script, filename = argv

    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CTRL-C(^C).")
    print("If you do want that, hit RETURN.")

    input("?")

    # 打开文件
    print("Opening the file...")
    target = open(filename, 'w')

    print("Truncating the file. Goodbye!")

    # 清空文件
    target.truncate()

    print("Now I'm going to ask you for three lines.")

    line1 = input("line1:")
    line2 = input("line2:")
    line3 = input("line3:")

    print("I'm going to write these to the file.")

    # 往文件中写入数据
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print("And finaly, we close it.")
    # 关闭文件对象
    target.close()

    file2 = open(filename, "r")

    print(file2.read())

    file2.close()

# 脚本的入口点，被当作模块调用的时候不会执行。
if __name__ == "__main__":
    # 调用 main()
    main()
