#!/usr/bin/python3

import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]

    total = 0

    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

        print ("{}".format(total))
