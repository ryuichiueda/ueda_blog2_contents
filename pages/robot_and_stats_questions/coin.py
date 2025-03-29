#!/usr/bin/python3

import sys

prob_a = 0.5

A_TOP = 0.5
A_BACK = 0.5
B_TOP = 1.0/3
B_BACK = 2.0/3

for c in sys.stdin:
    c = c.strip()
    if c == "表":
        prob_a = A_TOP*prob_a/(A_TOP*prob_a + B_TOP*(1.0 - prob_a))
    if c == "裏":
        prob_a = A_BACK*prob_a/(A_BACK*prob_a + B_BACK*(1.0 - prob_a))

print(prob_a)
