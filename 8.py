'''Даны два неупорядоченных набора целых чисел  (может быть, с повторениями).  
Выдать без повторений в порядке возрастания все те числа, которые 
встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во 
элементов  первого множества. m — кол-во элементов второго 
множества. Затем пользователь вводит сами элементы множеств.
'''

def fillArray(n):
    
    list = []
    for i in range(n):
        num = int(input("Введите число: "))
        list.append(num)

    return list

def common_el(arr, arr2):
    sorted_arr = sorted(arr)
    sorted_arr2 = sorted(arr2)
    common_list = []
    i = j = 0
    while i < len(sorted_arr) and j < len(sorted_arr2):
            if sorted_arr[i] == sorted_arr2[j]:
                common_list.append(sorted_arr[i])
                i += 1
                j += 1
            elif sorted_arr[i] < sorted_arr2[j]:
                 i += 1
            else:
                 j += 1
            print(common_list)
            


n = int(input("Введите количество элементов первого множества: "))
list1 = fillArray(n)
print(list1)
m = int(input("Введите количество элементов второго множества: "))
list2 = fillArray(m)
print(list2)
k = common_el(list1, list2)
print(k)
