
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in my_array:

    j = 2
    if i % j == 0 and i != j:
        my_array.remove(i)
    else:
        continue


print(my_array)