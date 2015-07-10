#!/usr/bin/env python2

import random
import sys

# choose a permutation
A = ord('A')
ALPHA = map(chr, range(A,ord('Z')+1))
random.shuffle(ALPHA)
while ALPHA[ord('E')-A] == 'E' or ALPHA[ord('T')-A] == 'T':
    random.shuffle(ALPHA)

for line in sys.stdin.readlines():
    for ch in line:
        ch = ch.upper()
        if 'A' <= ch <= 'Z':
            print ALPHA[ord(ch)-A],
        else:
            print ch,
    print
