import random

#task1
a = input('+-*/ -> ')
if '+' in a:
    print(int(a[ : a.index('+')]) + int(a[a.index('+')+1 : ]))
if '-' in a:
    print(int(a[ : a.index('-')]) - int(a[a.index('-')+1 : ]))
if '*' in a:
    print(int(a[ : a.index('*')]) * int(a[a.index('*')+1 : ]))
if '/' in a:
    print(int(a[ : a.index('/')]) / int(a[a.index('/')+1 : ]))

#task2

b = []
plus = 0
minus = 0
a = input('list len -> ')
# a = input('list -> ').split()
# for i in range(len(a)):
#     b.append(int(a[i]))

for i in range(int(a)):
    b.append(random.randint(-100, 100))
    if b[i] < 0:
        minus += 1
    if b[i] > 0:
        plus += 1

b.sort()
print(b)

print(f'min = {b[0]}')
print(f'max = {b[-1]}')
print(f'- -> {minus}')
print(f'+ -> {plus}')
print(f'0 -> {len(b)-minus-plus}')
