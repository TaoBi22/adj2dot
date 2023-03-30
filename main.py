#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <adjacency matrix file>")
else:
    with open(sys.argv[1]) as matFile:
        names = matFile.readline().strip().split(",")

        mat = [line.split(",") for line in matFile.read().splitlines()]

        doneEdges = []

        rep = "graph graphname {"

        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if int(val) == 1 and ((j, i) not in doneEdges):
                    rep += f"{names[i]} -- {names[j]};\n"
                    doneEdges.append((i, j))

        rep += "}"

        print(rep)
