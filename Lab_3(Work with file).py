try:
    import codecs
    import json
except:
    print("Import Error")


def create_file():
    f = open('D:\SYAP\Laba','a')
    str = " "
    while str != "":
        str = input("Введите слово которое хотите записать в файл\n")
        if str != "":
            f.write(str + '\n')
    f.close()
def open_file():
    create_file()
    f = open('D:\SYAP\Laba', 'r')
    z = open('D:\SYAP\Laba_@','w')
    max_count = 0
    max_word = ""
    for strop in f.readlines():
        if strop.find(" ") == -1:
            z.write(strop + '\n')
            count = 0
            for k in strop:
                dtr = k
                count += 1
            if max_count <= count:
                max_word = strop
                max_count = count
    print(max_word)
    f.close()
    z.close()

def read_cinema():
    f = open('D:\SYAP\Cinema','r', encoding = 'utf-8')
    data = input("Введите дату для поиска фильмов:\n")
    str = ""
    maxs = 0
    max = 0
    for text in f:
        stok = text.split()
        if stok[1] == data:
            print(text)
        max = int(stok[3])
        if int(maxs) <= int(max):
            maxs = int(stok[3])
            str = stok
    print(f"Самый посещаемый фильм ->{str}")
    f.close()

def create_dict():
    f = open('D:\SYAP\Hour','r',encoding = 'utf-8')
    my_dict = {}
    for text in f:
        i = 0
        sum = 0
        stok = text.split()
        for k in stok:
            i += 1
            if i == 2 or i == 3 or i == 4:
                try:
                    sum = sum + int(k.replace("(л)",''))
                except:
                    try:
                        sum = sum + int(k.replace("(пр)", ''))
                    except:
                        sum = sum + int(k.replace("(лаб)", ''))

        my_dict[stok[0]] = sum
    print(my_dict)
    f.close()

def json_company():
        with codecs.open('D:\SYAP\componis', 'r', 'utf_8_sig') as F, codecs.open('JSON.json', 'w', 'utf_8_sig') as java:
            profit = {}
            average = {}
            spisok = []
            lines = 0
            average_profit = 0
            for line in F:
                lines += 1
                line = line.split()
                price = 0
                sch = 1
                for i in line:
                    if i.isalpha() and i.isupper() == False:
                        key = i
                    if i.isdigit():
                        if sch % 2 == 1:
                            price += int(i)
                            sch += 1
                        else:
                            price -= int(i)
                average_profit += price
                profit.update({key: price})
            average.update({'Средняя прибыль': average_profit / lines})
            spisok.append(profit)
            spisok.append(average)
            print(spisok)
            json.dump(spisok, java)


def main():
    print("Первое задание:")
    open_file()
    print("---------------------------------------------------------")
    print("Второе задание:")
    read_cinema()
    print("Третье задание:")
    create_dict()
    print("Четвёртое задание:")
    json_company()

if __name__ == "__main__":
    main()