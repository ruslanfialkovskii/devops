#!/usr/bin/env python3.10
import os, json, glob, shutil 

try:
    os.mkdir('./processed')
except OSError:
    print("Folder exist")

subtotal = 0.0

for path in glob.iglob('./new/reciept-[0-9]*.json'):
    with open(path) as file:
        content = json.load(file)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"Move '{path}' to '{destination}'")

print(f"Reciept total: '{round(subtotal, 2)}'")