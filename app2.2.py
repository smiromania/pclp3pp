#app2.1


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

# nu se poate compara la sortare string cu int

# a = b = c = d = 1
# print(type(a))
# F22
