a = input("Введите 1 число: ")
b = input("Введите 2 число: ")
c = input("Введите 3 число: ")

if a > b and a > c:
    print("Число 1 самое большое")
    print(a)
elif b > a and b > c:
    print("Число 2 самое большое")
    print(b)
elif c > a and c > b:
    print("Число 3 самое большое")
    print(c)
else:
    print("2 или 3 больших числа равны")