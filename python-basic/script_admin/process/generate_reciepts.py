#!/usr/bin/env python3.10

# use random and json libs
import json
import random
import os

count = int(os.getenv("FILE_COUNT") or 10)
print(count)
words = [word.strip() for word in open("/usr/share/dict/words").readlines()]

for identifier in range(count):
    ammount = random.uniform(1.0,1000)
    content = {"topic": random.choice(words),
               "value": "%.2f" % ammount
               }
    with open(f"./new/reciept-{identifier}.json","w") as f:
        json.dump(content, f)