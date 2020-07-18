"""
While Loop

while predicate:
    code

predicate --> code --> predicate --> code --> predicate --> false --> loop end
(condition --> code) --> condition false --> loop end
"""

# infinite loop
# while True:
#     print('hello world')

i = 0
while i < 5:
    print(i)
    i += 1 # i = i + 1

print('i am outside loop')
