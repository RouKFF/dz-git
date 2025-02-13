from random import randint

a = [randint(-100, 100) for _ in range(20)]
a.sort()
print(a)
b = [randint(-100, 100) for _ in range(20)]
b.sort()
print(b)

oba = a + b
oba.sort()

oba_set = list(set(a+b))
oba_set.sort()

obshie = [x for x in a if x in b]
obshie.sort()

hz =  [i for i in a if a.count(i) == 1] + [j for j in b if b.count(j) == 1]
hz.sort()

minmax = [a[0], a[-1], b[0], b[-1]]


print(oba_set)
print()
print(obshie)
print()
print(hz)
print()
print(minmax)