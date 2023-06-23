#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение).


mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
myset_1 = set()
myset_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    myset_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    myset_2.add(i)
lok = myset_1 & myset_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')

