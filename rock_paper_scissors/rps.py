#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  result = []
  possible = {1: "rock", 2: "paper", 3: "scissors"}
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')