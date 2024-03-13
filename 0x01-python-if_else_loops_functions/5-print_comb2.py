#!/usr/bin/python3
for n in range(00, 100):
    if n != 99:
        print(f"{n:02}", end=", ")
    else:
        print("{}".format(n))
