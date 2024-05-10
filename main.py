print("Задание 1")
a = str(input("Введите символы: "))
b = 0
c = []
for s in a:
    if b%2 == 0:
        b+=1
        c.append(s.upper())
    else:
        b+=1
        c.append(s.lower())
print(c)

print("Задание 2")
a = int(input("Введите число: "))
if a > 1000:
    print("Ваше число болье 1000")
else:
    for i in range(a):
        print(i)

print("Задание 3")
a = []
for b in range(5+1):
    z = int(input("Введите число: "))
    a.append(b)
a.reverse()
for c in a:
    print(c)
