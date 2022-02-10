from random import randint
n=20
a=[]
for i in range(n):
    a.append(randint(1,99))
print(a)
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)