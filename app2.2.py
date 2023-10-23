#liste si tuple


l1 = [1, '2', '3']

for i in l1:
    print(i)
for i in range(len(l1)):
    print(l1[i])
for i, j in enumerate(l1):
    print(i, j)

l2 = [int(x) * 2 for x in l1]
print(l2)

for i, j in zip(l1, l2):
    print(i, j)

print(sorted([str(elem) for elem in l1]))
print(sorted([str(elem) for elem in l2]))


t1 = ('abcd', 786, 2.23, 'ion', 70.2)
t1 = ('xyz',) + t1[1:] #nu se poate muta in tuplu
print(len(t1))
t2=tuple(l2)
print(min([x for x in t1 if isinstance(x, (int, float))]))
print(min(t2))
t1_sorted = tuple(sorted([x for x in t1 if isinstance(x, (int, float))]))

print(t1_sorted)
# nu se poate compara la sortare string cu int

# a = b = c = d = 1
# print(type(a))
# F22
