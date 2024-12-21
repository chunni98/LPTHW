#!/usr/bin/env python3
# -*- coding: utf-8 -*-

formatter = "{} {} {} {}"
# 调用 formatter 的format 方法，结果作为 print 函数的参数。
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))
