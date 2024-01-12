#!/usr/bin/env python3.10

# test errors handling

import argparse
import sys
# build parser
parser = argparse.ArgumentParser(description="Read and reverse file")
parser.add_argument("file", type=str, help="input file")
parser.add_argument("-l", "--limit", type=int, help="set limit")
parser.add_argument("--version", action='version', version="%(prog)s 1.0")
# parse arguments
args = parser.parse_args()
# read file and reverse content
try:
    f = open(args.file)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
else:
    with open(args.file) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
