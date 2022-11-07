import matchcaselib
from numpy import arccos, sqrt, pi, sin, log10, mean
import matplotlib.pyplot as plt
import numpy as np


def task_1(x, a):
    z = arccos(x ** 2) - (a * sqrt(x / a ** 3)) + ((sin(pi / 2) ** 3) / log10(2 * x))
    return z


def task_2():
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    import matchcaselib

    def print_menu():
        print("\n 1 | Проверить на пропуски\n"
              " 2 | Проверить на нормальность распределения и выбросы\n"
              " 3 | Обработать пропуски\n"
              " 4 | Определить количество определенных квартир\n"
              " 5 | Построить сводную таблицу\n"
              " 6 | Выход")

    def checking_for_omissions(test):
        for col, dat in test.items():
            skip = test[test[col].isnull()]
            if not skip.empty:
                print(f"В {col} были замечены пропуски")

    def checking_for_distribution_and_emissions(test):
        for i in range(len(test.columns)):
            print(f"{i + 1} | {test.columns[i]}")
        number_of_graf = int(input("Выберите величину: ")) - 1
        values_of_graf = test.columns[number_of_graf]
        entered_graf = int(input(" 1 | Ящик с усами\n 2 | Гистограмма\n"))

        if entered_graf == 1:
            plt.title(test.columns[number_of_graf])
            plt.boxplot(test[values_of_graf])
        elif entered_graf == 2:
            plt.title(test.columns[number_of_graf])
            plt.hist(test[values_of_graf])
        plt.show()

    def fill_gaps(test):
        for col_name, data in test.items():
            skips = test[test[col_name].isnull()]
            if not skips.empty:
                test[col_name] = input(f"Чем заменить пропуски в {col_name} ->")

    def determine_number_of_rooms(test):
        amount_of_flats = pd.pivot_table(test, values="Id", index=["Rooms"], aggfunc=np.size, fill_value=0)
        print(f"Количество квартир:"
              f"\n{amount_of_flats}")

    def build_pivot_table(test):
        frame_info = pd.pivot_table(data_test, values="Id", index=["DistrictId"],
                                    columns=["Rooms"], aggfunc=np.size, fill_value=0)
        print(f"Сводная таблица:\n{frame_info}")
        test.to_csv("surname.csv")

    data_test = pd.read_csv("test.csv", sep=",")
    data_test = data_test.head(1000)
    a = True
    while a:
        print_menu()
        try:
            while a:
                choice = int(input("Выберите операцию -> "))
                with matchcaselib.match(choice) as m:
                    if m.case(1):
                        checking_for_omissions(data_test)
                    if m.case(2):
                        checking_for_distribution_and_emissions(data_test)
                        break
                    if m.case(3):
                        fill_gaps(data_test)
                        break
                    if m.case(4):
                        determine_number_of_rooms(data_test)
                        break
                    if m.case(5):
                        build_pivot_table(data_test)
                        break
                    if m.case(6):
                        a = False
        except ValueError:
            print("Некорректный ввод!")


def task_3(x, c):
    l = (abs((2 * x - c))) ** (3 / 5) + 0.567
    return l


def task_4():
    def first_function(a, b):
        return a ** 0.25 - b ** 0.25

    def second_function(a, b):
        return a ** 2 - b ** 2

    def third_function(a, b):
        return 2 * a + 3 * b

    def fourth_function(a, b):
        return a ** 2 + b ** 2

    def fifth_function(a, b):
        return 2 + 2 * a + 2 * b + a ** 2 - b ** 2

    def print_menu():
        print("\n 1 | x^0.25 + y^0.25"
              "\n 2 | x^2 - y^2"
              "\n 3 | 2x + 3y"
              "\n 4 | x^2 + y^2"
              "\n 5 | 2 + 2x + 2y - x^2 - y^2"
              "\n 6 | Выход")

    while True:
        print_menu()
        try:
            x = np.linspace(-50, 50)
            y = np.linspace(-50, 50)

            X, Y = np.meshgrid(x, y)

            while True:
                user_choice = int(input("Выберите функцию -> "))
                if 6 < user_choice < 1:
                    raise ValueError

                with matchcaselib.match(user_choice) as m:
                    if m.case(1):
                        x = np.linspace(0, 50)
                        y = np.linspace(0, 50)

                        A, B = np.meshgrid(x, y)
                        Z = first_function(A, B)
                        break
                    if m.case(2):
                        Z = second_function(X, Y)
                        break
                    if m.case(3):
                        Z = third_function(X, Y)
                        break
                    if m.case(4):
                        Z = fourth_function(X, Y)
                        break
                    if m.case(5):
                        Z = fifth_function(X, Y)
                        break
                    if m.case(6):
                        print("До свидания!")
                        exit(0)
            ax = plt.axes(projection='3d')
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                            cmap='viridis')
            plt.show()
        except ValueError:
            print("Некорректный ввод!")


def main():
    # arr = []
    # print("(Задание 1)Вычислите выражение:")
    # print(task_1(x=0.093, a=0.94 * 10 ** -3))
    # print("(Задание 2)Работа с Pandas и визуализация данных в Matplotlib:")
    # task_2()
    # print("(Задание 3) Визуализация данных в Matplotlib:")
    # index = 0
    # arr_i = []
    # fix, ax = plt.subplots()
    # for i in range(-10, 1):
    #     arr.append(task_3(12.1, i))
    #     arr_i.append(i)
    #     plt.plot(i, arr[index], color='black', marker='s')
    #     print(f"Аргумент:{i}\n"
    #           f"Значение:{arr[index]}")
    #     index += 1
    #
    # print(f"Максимальный элемент->{max(arr)}")
    # print(f"Минимальный элемент->{min(arr)}")
    # print(f"Среднее значение массива->{mean(arr)}")
    # print(f"Количество элементов массива->{len(arr)}")
    # s = int(mean(arr))
    # plt.plot(s, s + 1, marker="s")
    # plt.xlabel("Аргумент")
    # plt.ylabel("Значение")
    # plt.show()
    task_4()


if __name__ == "__main__":
    main()
