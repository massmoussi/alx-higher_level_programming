#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    values = dir(hidden_4)
    for name in values:
        if name[:2] != "__":
            print(name)
