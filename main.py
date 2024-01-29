# var 2: 2, б, д, е:
# Массив данных библиотечных книг: ФИО автора,  название, год издания, количество страниц
# (сравнение по  полям - ФИО автора, название, год издания)
# Сортировка пузырьком
# Пирамидальная сортировка
# Быстрая сортировка
# https://www.kaggle.com/datasets/chrico03/art-garfunkels-library?resource=download
import pandas as pd
import time
import matplotlib.pyplot as plt

from bubble_sort import my_bubblesort
from heap_sort import heapSort
from quick_sort import quick_sort

# @brief скачиваю данные с Kaggle и подготавливаю их для работы, разбивая на разные размеры.
df = pd.read_csv('Art Garfunkel Library.csv') # dataset No 1

df_1 = df[:100]
df_1 = df_1.drop(["Date Read", "Favorite"], axis=1)
print(len(df_1)) # 100
df_1.to_csv("data_1.csv")
df_2 = df[100:220]
df_2 = df_2.drop(["Date Read", "Favorite"], axis=1)
print(len(df_2)) # 120
df_2.to_csv("data_2.csv")
df_3 = df[220:350]
df_3 = df_3.drop(["Date Read", "Favorite"], axis=1)
print(len(df_3)) # 130
df_3.to_csv("data_3.csv")
df_4 = df[350:490]
df_4 = df_4.drop(["Date Read", "Favorite"], axis=1)
print(len(df_4)) # 140
df_4.to_csv("data_4.csv")
df_5 = df[490:640]
df_5 = df_5.drop(["Date Read", "Favorite"], axis=1)
print(len(df_5)) # 150
df_5.to_csv("data_5.csv")
df_6 = df[640:800]
df_6 = df_6.drop(["Date Read", "Favorite"], axis=1)
print(len(df_6)) # 160
df_6.to_csv("data_6.csv")
df_7 = df[800:970]
df_7 = df_7.drop(["Date Read", "Favorite"], axis=1)
print(len(df_7)) # 170
df_7.to_csv("data_7.csv")
df_8 = df[970:1150]
df_8 = df_8.drop(["Date Read", "Favorite"], axis=1)
print(len(df_8)) # 180
df_8.to_csv("data_8.csv")


# print(df_7)

# df = pd.read_csv('data_1.csv')
# print(df)
# for i in df:
#     print(type(i), i)
# @brief класс нашего объекта. Именно относително него и будут перегружены операторы >, <, >=, <=
class obj:
    def __init__(self, author:str, book:str, year:int, pages:int):
        self.author = author
        self.book = book
        self.year = year
        self.pages = pages
    # @brief <
    def __lt__(self, other): # <
        if self.author < other.author:
            return True
        elif self.author > other.author:
            return False
        else:
            if self.book < other.book:
                return True
            elif self.book > other.book:
                return False
            else:
                if self.year < other.year:
                    return True
                else:
                    return False
    # @brief <=
    def __le__(self, other): # <=
        if self.author < other.author:
            return True
        elif self.author > other.author:
            return False
        else:
            if self.book < other.book:
                return True
            elif self.book > other.book:
                return False
            else:
                if self.year < other.year:
                    return True
                elif self.year > other.year:
                    return False
                else:
                    return True
    # @brief >
    def __gt__(self, other): # >
        if self.author > other.author:
            return True
        elif self.author < other.author:
            return False
        else:
            if self.book > other.book:
                return True
            elif self.book < other.book:
                return False
            else:
                if self.year > other.year:
                    return True
                else:
                    return False
    # @brief >=
    def __ge__(self, other): # >=
        if self.author > other.author:
            return True
        elif self.author < other.author:
            return False
        else:
            if self.book > other.book:
                return True
            elif self.book < other.book:
                return False
            else:
                if self.year > other.year:
                    return True
                elif self.year < other.year:
                    return False
                else:
                    return True

    def __eq__(self, other): # ==
        if self.author != other.author:
            return False
        if self.book != other.book:
            return False
        if self.year != other.year:
            return False
        return True


# a = obj("b",'c',2,1)
# b = obj("b",'b',2,1)
# print(a>=b)
# @brief тут я готовлю массивы данных, чтобы отправлять их в функции сортировки, как и требуется в задании
df_1 = pd.read_csv('data_1.csv')
mas_1 = []
l = len(df_1)
for i in range(l):
    mas_1.append(obj(df_1['Author'][i], df_1['Books'][i], df_1['Year Published'][i], df_1['Pages'][i]))
# print(len(mas_1))

df_2 = pd.read_csv('data_2.csv')
mas_2 = []
l = len(df_2)
for i in range(l):
    mas_2.append(obj(df_2['Author'][i], df_2['Books'][i], df_2['Year Published'][i], df_2['Pages'][i]))
# print(len(mas_2))

df_3 = pd.read_csv('data_3.csv')
mas_3 = []
l = len(df_3)
for i in range(l):
    mas_3.append(obj(df_3['Author'][i], df_3['Books'][i], df_3['Year Published'][i], df_3['Pages'][i]))
# print(len(mas_3))

df_4 = pd.read_csv('data_4.csv')
mas_4 = []
l = len(df_4)
for i in range(l):
    mas_4.append(obj(df_4['Author'][i], df_4['Books'][i], df_4['Year Published'][i], df_4['Pages'][i]))
# print(len(mas_4))

df_5 = pd.read_csv('data_5.csv')
mas_5 = []
l = len(df_5)
for i in range(l):
    mas_5.append(obj(df_5['Author'][i], df_5['Books'][i], df_5['Year Published'][i], df_5['Pages'][i]))
# print(len(mas_5))

df_6 = pd.read_csv('data_6.csv')
mas_6 = []
l = len(df_6)
for i in range(l):
    mas_6.append(obj(df_6['Author'][i], df_6['Books'][i], df_6['Year Published'][i], df_6['Pages'][i]))
# print(len(mas_6))

df_7 = pd.read_csv('data_7.csv')
mas_7 = []
l = len(df_7)
for i in range(l):
    mas_7.append(obj(df_7['Author'][i], df_7['Books'][i], df_7['Year Published'][i], df_7['Pages'][i]))
# print(len(mas_7))

df_8 = pd.read_csv('data_8.csv')
mas_8 = []
l = len(df_8)
for i in range(l):
    mas_8.append(obj(df_8['Author'][i], df_8['Books'][i], df_8['Year Published'][i], df_8['Pages'][i]))
# print(len(mas_8))

mass = [mas_1, mas_2, mas_3, mas_4, mas_5, mas_6, mas_7, mas_8]
# @brief Формирую, так же, координаты по х для графиков: размеры массивов
x = []
for i in mass:
    x.append(len(i))
print(x)

# @brief сортировка пузырьком
bubble_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    my_bubblesort(tmp)
    bubble_times.append(time.time() - start)
    with open(f'bubble_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.author} {elem.book} {elem.year} {elem.pages}\n')
print(bubble_times)
plt.plot(x, bubble_times)

# @brief пирамидальная сортировка
heap_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    heapSort(tmp)
    heap_times.append(time.time() - start)
    with open(f'heap_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.author} {elem.book} {elem.year} {elem.pages}\n')
print(heap_times)
plt.plot(x, heap_times)

# @brief быстрая сортировка
quick_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    tmp = quick_sort(tmp)
    quick_times.append(time.time() - start)
    with open(f'quick_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.author} {elem.book} {elem.year} {elem.pages}\n')
print(quick_times)
plt.plot(x, quick_times)
# @brief отрисовка графиков
plt.legend(('bubble', 'heap', 'quick'))
plt.show()

