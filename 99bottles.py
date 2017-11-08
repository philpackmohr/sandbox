#!/usr/bin/python

bob = "bottles of beer"
otw = "on the wall"
todpia = "take one down, pass it around,"

for i in range(99, 0, -1):  # range from 99 to 1
    print(i, bob, otw, i, bob + ",",
          todpia, i-1, bob, otw)
