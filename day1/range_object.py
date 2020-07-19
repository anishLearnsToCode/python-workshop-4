"""
Range

range(stop)
range(start, stop)
range(start, stop, step)

step default = 1
start default = 0
stop default XXXXX

iterable object
"""

r = range(5, 10, 3)
print(r)
# print(type(r))
# print(r.start)
# print(r.stop)
# print(r.step)

for i in range(5, 10, 3):
    print(i)

