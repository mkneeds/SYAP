

def searchGregory(number):
    pi = 0
    for i in range(number):
        pi += 4 * (-1) ** i / (2 * i + 1)
    return pi

def searchVD(str):
    count_VO = 0
    count_CON = 0
    vowels_EU = set("aeiou")
    vowels_RU = set("Ауоыиэяюёе")

    for letter in str:
        if letter in vowels_EU or letter in vowels_RU:
            count_VO += 1
        else:
            count_CON += 1
    print(f"Количество гласных равно:{count_VO}")
    print(f"Количество согласных равно:{count_CON}")

def separateList():
    _str = [1,34,'qwerty', 12, 13, 16,'Love', 'Python']
    list_I = []
    list_S = []
    sum = 0

    for i in _str:
        try:
            check = int(i)
            list_I.append(i)
            sum += i
        except:
            list_S.append(i)
    print(f"Список чисел->{list_I}, Сумма чисел->{sum}")
    print(f"Список строковых->{list_S}")

def swapStrInDict():
    _str = "An apple a day keeps the doctor away"
    dictionary = {symbol: _str.count(symbol) for symbol in _str}
    print(dictionary)

response = {}
balance = 100

def addParts():

    add_active = True
    while add_active:
        name = input("Введите название товара:")
        structure = []
        structure.append(input("Введите(Состав):"))
        try:
            structure.append(int(input("Введите(Кол-во):")))
            structure.append(int(input("Введите(Цену):")))
        except:
            print("Неверный Формат.Повторите попытку")
            structure.append(int(input("Введите(Кол-во):")))
            structure.append(int(input("Введите(Цену):")))
        response.setdefault(name, [])
        response[name].append(structure)
        print("Товар успешно добавлен")
        con = input("Добавить ещё?(Да/Нет)")
        if con in "Нет" or con in "нет":
            add_active = False
    return response

def getStructure():
    count = 1
    for name in response:
        print(f"{count}.Название товара -> {name}")
        count += 1
        for st in response[name]:
            for i in st:
                print(f" Состав товара->{i}")
                break

def getPrice():
    for name in response:
        _count = 1
        _ruller = 0
        print(f"{_count}.Название товара -> {name}")
        _count += 1
        for st in response[name]:
            for i in st:
                _ruller += 1
                if _ruller == 3:
                    print(f" Цена товара->{i}")
                    break

def getCount():
    for name in response:
        _count = 1
        _ruller = 0
        print(f"{_count}.Название товара -> {name}")
        _count += 1
        for st in response[name]:
            for i in st:
                _ruller += 1
                if _ruller == 2:
                    print(f" Кол-во товара->{i}")
                    break
def getFull():
    for name in response:
        _count = 0
        _check = 0
        print(f"{_count}.Название товара -> {name}")
        for st in response[name]:
            for i in st:
                if _check == 0:
                    print(f"Состав товара->{i}")
                if _check == 1:
                    print(f"Кол-во товара->{i}")
                if _check == 2:
                    print(f"Цена товара->{i}")
                _check += 1
        _count += 1

def buyProduct():
    _count = 0
    arr = []
    new_opr = []
    new_response = {}
    if response:
        print("Название товаров которое можно купить:")
        a = list(response)
        i = 0
        for key in response:
            arr.append(key)
            print(f"{_count}.{key}")
            _count += 1
        try:
            c_product = int(input("Введите цифру товара которого хотите купить->"))
            val = int(input("Сколько вы хотите купить?"))
        except:
            print("Неверный Формат.Повторите попытку")
            c_product = int(input("Введите цифру товара которого хотите купить->"))
            val = int(input("Сколько вы хотите купить?"))
        flag = 0
        flag_b = False
        for z in response[arr[c_product]]:
            for key in z:
                if flag == 0:
                    new_opr.append(key)
                elif flag == 2:
                    if flag_b == True:
                        if balance >= key:
                            new_opr.append(int(key))
                            flag_b = True
                        else:
                            print("Недостаточное количество средств")
                            flag_b = False
                elif flag == 1:
                    if key >= val:
                        flag_b = True
                        new = key - val
                        new_opr.append(int(new))
                    else:
                        print("Недостаточное количество")
                        flag_b = False

                flag += 1
        if flag_b:
            new_response.setdefault(arr[c_product], [])
            new_response[arr[c_product]].append(new_opr)
            response.update(new_response)

    else:
        print("Нет товаров!!!")




def shopAutoParts():
    menu = True
    while menu:
        choose = input("""                          
                          1. Добавить товар
                          2. Просмотр описания: название – описание
                          3. Просмотр цены: название – цена.
                          4. Просмотр количества: название – количество.
                          5. Всю информацию.
                          6. Покупка
                          7. Выход
Ваш выбор:""")
        if choose in "1":
            addParts()
        elif choose in "2":
            getStructure()
        elif choose in "3":
            getPrice()
        elif choose in "4":
            getCount()
        elif choose in "5":
            getFull()
        elif choose in "6":
            buyProduct()
        elif choose in "7":
            print("До свидания")
            menu = False
        else:
            print("Неверный выбор. Повторите попытку")

def getMinCort():
    cort = (1,'f','232',12,7)
    min = cort[0]
    for k in cort:
        try:
            if k % 2 == 0:
                min = k
        except:
            print("")

    for a in cort:
        try:
            if a % 2 == 0:
                if a < min:
                    min = a
        except:
            print("")
    print(f"Минимальный четный элемент->{min}")
    if min == None:
        print("В кортеже не обнаружено числа")
        print(f"Вывожу первый элемент->{cort[0]}")



def main():
    print(f"Первое задание:(вычисления числа Пи по формуле Грегори, взяв 500 членов ряда->{searchGregory(500)}")
    print("Второе задание: Определить, сколько в строке гласных, а сколько согласных")
    str = input("Введите строку:")
    searchVD(str)
    print("Третье задание: Создать отдельно список из слов и отдельно из чисел.")
    separateList()
    print("Четвертое задание: Создайте словарь из строки")
    swapStrInDict()
    print("Пятое задание: «Магазин автозапчастей» ")
    shopAutoParts()
    print("Шестое задание: Найдите наименьший четный элемент кортежа")
    getMinCort()


if __name__ == '__main__':
    main()

