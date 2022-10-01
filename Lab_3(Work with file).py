def create_file():
    f = open('D:\SYAP\Laba','a')
    str = " "
    while str != "":
        flag = True
        str = input("Введите слово которое хотите записать в файл\n")
        if str != "":
            f.write(str + '\n')
    f.close()
def open_file():
    f = open('D:\SYAP\Laba', 'r')
    z = open('D:\SYAP\Laba_@','w')
    str = ""
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

def main():
    # print("Первое задание:")
    # create_file()
    # open_file()
    # print("---------------------------------------------------------")
    print("Второе задание:")
    read_cinema()


if __name__ == "__main__":
    main()