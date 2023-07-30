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
    arr.sort()
    arr2.sort()
    common_list = []
    print(arr, arr2)
    
    i = j = 0
    while i < len(arr) and j < len(arr2):
            if arr[i] == arr2[j]:
                common_list.append(arr[i])
                i += 1
                j += 1
            elif arr[i] < arr2[j]:
                i += 1
            else:
                j += 1
    return common_list   

n = int(input("Введите количество элементов первого множества: "))
list1 = fillArray(n)
m = int(input("Введите количество элементов второго множества: "))
list2 = fillArray(m)
k = common_el(list1, list2)
print(k)