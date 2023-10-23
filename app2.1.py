print()
l0 = ['abcd', 782, 2.23, 'john', 70 + 1j]
l1 = ['unu', 42 + 1j, 1.23, 'doi', 70.123]
l2 = list()

print(l1[2:])

l1[4:] = l1;
print(l1)

l2 = [123, 14]
l3 = l1 + l2
l1[1] = 69
print(l3)

l4 = l2
l2[0] = 'saisnoua'
print(l4)

l5 = [0, 0, 0, 0]
l5[0:1] = [1, 2]
l5.insert(1, [7, 7, 7, 7, 7, 7])
l5.insert(0, l5)
print(l5)

l5[:] = []

print(l5)

l6 = [l1, l2, l5]
l1[0] = 29

print(l6)

print(sorted([str(elem) for elem in l1]))
print(sorted([str(elem) for elem in l2]))

#nu se poate compara la sortare string cu int

print(len(l1))
print(len(l2))






# a = b = c = d = 1
# print(type(a))
# F22
