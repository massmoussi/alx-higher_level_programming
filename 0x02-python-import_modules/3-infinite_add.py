#!/usr/bin/python3

import sys
if __name__ == "__main__":
    num = 0
    lengt = len(sys.argv)

    for i in range(1, lengt):
        num += int(sys.argv[i])
    print(num)
