#!/usr/bin/env python

with open('DATA/salad.gif', 'rb') as salad_in:
    data = salad_in.read()

print(type(data))

s = "foo\u00B0\n"  # chars
b = b"bar\n" # bytes

print(s.encode())
print(b.decode())

