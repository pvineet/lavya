# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:29:20 2017

@author: vineetp
"""

a = 10
b = 10
c = a

print(a,b,c)

# trying out with immutable items
print(id(a))
print(id(b))
print(id(c))

print("python runtime optimisation into play here objects, some list of numbers are pre created -5 to 257")

a = "Hello World"
b = "Hello World"
c = a

# trying out with immutable items
print(id(a))
print(id(b))
print(id(c))

#Observing behaviour with mutable objects

a = [10,20,30]
b = [10,20,20]
c = a

print(a)
print(b)
print(c)

a[0] =  100

print(a)
print(b)
print(c)

print(id(a[0]))
print(id(a[1]))
print(id(c[0]))
print(id(b[1]))

