n = int(input("Число купленных карандашей: "))

if 0 <= n <= 10:
    if n == 0 or n >= 5:
        print("Я купил {0} карандашей".format(n))
    elif n == 1:
        print("Я купил {0} карандаш".format(n))
    elif n == 2 or n == 3 or n == 4:
        print("Я купил {0} карандаша".format(n))
else:
    print("Число карандашей может быть в диапазоне от 0 до 10")
