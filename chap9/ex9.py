#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the monts: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

import time,random

text = "你好，今天天气怎么样？"

for i in text:
    print(i, end="", flush=True)
    time.sleep(random.uniform(0.20,0.5))

print("\n")
