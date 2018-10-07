import math

#Ввод данных пользователем (10 чисел)
lst = []
print("Введите значения массива")

for i in range(10):
    lst.append(int(input()))
print("Вы ввели")
print(lst)

#Функция сортировки пузырьком
def PuzirokSort(array):

    n = 1
    while n < len(array):
         for i in range(len(array)-n):
              if array[i] > array[i+1]:
                   array[i],array[i+1] = array[i+1],array[i]
         n += 1
    return array

#Гномья сортировка
def GnomeSort(lst):
    i = 1
    while i < len(lst):
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return lst

#Блочная сортировка
def BucketSort (array, n):

    minEl = min(array)
    maxEl = max(array)

    buckets = []
    for i in range(n):
        buckets.append([])

    for i in range(len(array)):
        bucketsNumber = math.floor(n*(array[i] - minEl)/(maxEl - minEl))
        if (bucketsNumber == n):
            bucketsNumber -= 1
        buckets[bucketsNumber].append(array[i])
    for i in range(n):
        buckets[i].sort()
    returnArray = []

    for lst in buckets:
        for element in lst:
            returnArray.append(element)
    return returnArray

#Пирамидальная сортировка
def HeapSort(li):

    def downHeap(li, k, n):
        new_elem = li[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and li[child] < li[child+1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(size//2-1,-1,-1):
        downHeap(li, i, size)
    for i in range(size-1,0,-1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i)
    return li



print("Результат сортировки методом пузырька")
print(PuzirokSort(lst[:]))

print("Результат сортировки методом гнома")
print(GnomeSort(lst[:]))

print("Результат пирамидальной сортировки")
print(HeapSort(lst[:]))

print("Результат блочной сортировки c количеством блоков: 3")
print(BucketSort(lst[:],5))
