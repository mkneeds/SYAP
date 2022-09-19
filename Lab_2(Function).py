try:
    from collections import OrderedDict
    import random

except:
    print("Библиотека не врубилась")

def is_prime(n):
    book = {}
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            flag = "True"
            book[i] = flag
    print(book)

def check_arg(T1,T2,T3,T4):
    sum = 0
    if isinstance(T1,list):
        for i in T1:
            try:
                check = int(i)
                sum += i
            except:
                print("")
        print(sum)
    if isinstance(T2,dict):
        try:
            s = (OrderedDict(sorted(T2.items(), key=lambda t: t[1], reverse=True)))
            srez3 = list(s)[0:3]
            print("ТОП 3:")
            for key_srez in srez3:
                print(key_srez, ":", T2.get(key_srez))
        except:
            print("Содержит str")
    if isinstance(T3,int):
        sum = 0
        while (T3 != 0):
            sum = sum + T3 % 10
            T3 = T3 // 10
        print("Сумма цифр числа равна: ", sum)
    if isinstance(T4,str):
        result = len(T4.split())
        print(f"Число слов -> {result}")

def print_arr(str, col):
    for i in range(str):
        for j in range(col):
            print(arr[i][j], end=' ')
        print()
arr = []
def sumMatr():
    while 1:
        try:
            str = int(input('Введите количество строк массива: '))
            col = int(input('Введите количество столбцов массива: '))
        except ValueError:
            print('Ошибка!')
        else:
            break
    for i in range(str):
        arr.append([0] * col)
    for i in range(str):
        for j in range(col):
            while 1:
                try:
                    arr[i][j] = int(input())
                except ValueError:
                    print('Ошибка!')
                else:
                    break
    print('Исходная матрица:')
    print_arr(str, col)
    k = 0
    s = 0
    i = 0
    j = 0
    for j in range(col):
        for i in range(str):
            if arr[i][j] > 0:
                k += 1
            else:
                k = 0
                break
            if k == col:
                s = i
                break
    sum = 0
    for j in range(col):
            sum += arr[s][j]
    print(f"Строка под номером ->{s+1} содержит все положительные элементы. Сумма их равна ->{sum}")
def main():
    is_prime(5)
    a = [5,6,7]
    elements = {'1': 70,'2': 86266, '3': 324, '4': 1}
    chislo = 252
    str = "Привет друг"
    check_arg(a, elements,chislo,str)
    sumMatr()

if __name__ == "__main__":
    main()