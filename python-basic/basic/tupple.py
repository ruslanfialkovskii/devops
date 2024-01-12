#!/usr/bin/env python3.10
# immutable list 

point = (2.0, 3.0)

# this doesn't work -> point[1] = 4

# we can create new tupple
new_point = point + (4,)
print(new_point)

print("This is some interesting things %s %s." % ("Op", "Opa"))

print("This is some interesting things %s %s." % ["Op", "Opa"])