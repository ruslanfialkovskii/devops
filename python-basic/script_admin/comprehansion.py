#!/usr/bin/env python3.10

import argparse

parser = argparse.ArgumentParser(prog="Searcher",description="This programm search snippet text in file")
parser.add_argument("filename")
parser.add_argument("search")
args = parser.parse_args()

#matches = []

with open(args.filename) as f:
    list_words = f.readlines()
#    print(list_words)
#    for word in list_words:
#        if args.search in word.lower():
#            matches.append(word)
# replcae with comprehansion

matches = [word.strip() for word in list_words if args.search in word.lower()]

print(matches)