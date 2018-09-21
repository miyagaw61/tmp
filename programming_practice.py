#!/usr/bin/env python3

"""
$ cat example01
6 3
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
4 5 6 1 2 3
4 5 6 1 2 3
4 5 6 1 2 3

$ cat example01 | python hoge.py
2 5
5 2

$ cat example02
6 2
76 251 15 224 89 129
90 129 102 161 14 92
78 180 218 236 47 25
96 126 138 37 59 202
43 213 30 105 29 195
132 19 14 166 106 16

$ cat example02 | python hoge.py
136 125 81
120 157 83
101 78 86
"""

def get_onelines(src, k):
    for i in range(len(src)):
        victim_line = src[i]
        for j in range(0, len(victim_line), k):
            oneline = victim_line[j:j+k]
            yield oneline

def get_boxes(onelines, k, line_length):
    splited_onelines = [onelines[i:i+k*line_length] for i in range(0, len(onelines), k*line_length)]
    for splited_oneline in splited_onelines:
        for box_first_idx in range(line_length):
            yield [splited_oneline[i] for i in range(box_first_idx, k*line_length, line_length)]

def calc_average(boxes, k):
    for i, box in enumerate(boxes):
        s = 0
        for oneline in box:
            for x in oneline:
                s = s + int(x)
        ave = int(s / (k*k))
        print(ave, end="")
        if (i+1) % line_length == 0:
            print()
        else:
            print(" ", end="")

data = input()
n, k = [int(x) for x in data.split(" ")]
line_length = int(n / k)

src = []
for i in range(n):
    src.append(input().split(" "))

onelines = list(get_onelines(src, k))
boxes = list(get_boxes(onelines, k, line_length))
calc_average(boxes, k)
