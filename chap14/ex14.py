#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#      Copyright:  (C) 2024 shachi All rights reserved.
#
#           File: chap14/ex14.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
from sys import argv

def main():
    script, user_name = argv
    prompt = "\" "

    print(f"Hi {user_name}, I'm the {script} script")
    print("I'd like to ask you a few question.")
    print(f"Do you like me {user_name}?")
    likes = input(prompt)

    print(f"Where do you live {user_name}?")
    lives = input(prompt)

    print("What kind of computer do you have?")
    computer = input(prompt)

    print(f"""
Alright, so you said {likes} about likeing me.
You live in {lives}. Not sure where thta is.
And you have a {computer}. Nice.
    """)

if __name__ == "__main__":
    main()
