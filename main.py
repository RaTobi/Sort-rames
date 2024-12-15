array = [68, 36, 254, 3215, 641, 6874, 78, 2, 32, 91] #ukol cislo 1

def bubble_sort():#ukol cislo 2
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
    return array

bubble_sort()
array
print('--------serazene pomoci bubble sortu--------')
