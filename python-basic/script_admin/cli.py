#!/usr/bin/env python3.10

# import sys
# # test some arguments in cli
# print(f"First argument {sys.argv[1:]}")
# print(f"First argument {sys.argv[1]}")

# test argparse

import argparse

# build parser
parser = argparse.ArgumentParser(description="Read and reverse file")
parser.add_argument("file", type=str, help="input file")
parser.add_argument("-l", "--limit", type=int, help="set limit")
parser.add_argument("--version", action='version', version="%(prog)s 1.0")
# parse arguments
args = parser.parse_args()
# read file and reverse content
with open(args.file) as f:
    lines = f.readlines()
    lines.reverse()
    
    if args.limit:
        lines = lines[:args.limit]
    
    for line in lines:
        print(line.strip()[::-1])