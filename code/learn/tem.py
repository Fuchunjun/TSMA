def tem(list):
    list.append(3)

    return (list[0], list)

list=[1, 2, 3, 4, 5]

a,b=tem(list)

print(a)
print(b)