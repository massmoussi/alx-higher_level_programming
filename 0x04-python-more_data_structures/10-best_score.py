#!/usr/bin/python3
ef best_score(a_dictionary):
    if a_dictionary is None:
        return "None"
    else:
        mavalue = 0
        makey = None
        for k, v in a_dictionary.items():
            if mavalue < v:
                mavalue = v
                makey = k
        return makey
