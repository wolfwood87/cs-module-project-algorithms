#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, limit):
    items.sort(key = lambda x: x.value, reverse=True)
    #could be better sorted by value/weight ratio
    sack = []
    value = 0
    cur = 0
    for i in range(len(items)):
        print(i)
        if cur + items[i][1] <= limit:
            value += items[i][2]
            sack.append(items[i][0])
            cur += items[i][1]
    return {"Value": value, "Chosen": sack}


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')