#!/usr/bin/python3
for d1 in range(10):
    for d2 in range(d1 + 1, 10):
        comb = "{}{}".format(d1, d2)
        if d1 < 8 or d2 < 9:
            print(comb, end=", ")
        else:
            print(comb)
