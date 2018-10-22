from functools import partial
from random import shuffle

Q1 = [123, 354, 324, 2340, 324, 234, 756, 955]
maxValue = 0

for i in Q1:
    if i > maxValue:
        maxValue = i
    else:
        continue
print(maxValue)




#sorted_list = sorted(Q1)
#print(sorted_list)
#print(sorted_list[7])

q2 = [432, 435, "598", "464", 234]

for i in range(0, len(q2)):
    q2[i] = int(q2[i])
print(q2)

for i in range(0, len(q2)):
    q2[i] = str(q2[i])
print(q2)


q3 = ["K1: V1", "K2: V2", "K3: V3"]

#my_dict2 = {y:x for x, y in q3.items()}
#print(my_dict2)

#flipped_dict = dict(zip(q3.values(), q3.keys()))
#for key, value in q3:
    #key = key[value]

  #  print(q3)

q4 = (1, 2, 3, 4, 5)
#you can't

q5 = [50, 96, 45, 67, 88]
numFailed = 0
for i in q5:
    numFailed += i < 70
print(numFailed)

q6 = [33, 56, 76, 78, 34, 56]
for i in q6:
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 5 == 0 & i % 3 == 0:
        print("fizzbuzz")
    else:
        print("nope")

q6 = [33, 56, 76, 78, 45, 56]

for i in q6:
    fizzString = ""
    if i % 3 == 0:
        fizzString += "fizz"
    if i % 5 == 0:
        fizzString += "buzz"
    print("%i  %s" % (i, fizzString))


def formatter(text):
    return "*********\n" + text + "\n **********"
def printWithFormatter(formattingFunction, text):
    print(formattingFunction(text))


printWithFormatter(formatter, "hello there!\ngeneral kenobi\n*unsheathes four lightsabers*")

def sumOf(a, b):
    return a + b

print(sumOf(1, 3))

plusTwo = partial(sumOf, 2)
print(plusTwo(1))


namesList = ["Enrico", "James", "Ilyas", "Java", "Naazim", "Jon", "Mohammed", "Abidul", "Sabiha",
             "Trisha", "Mubeen", "Prabat", "Jay", "Jonah", "Jameson", "Thefirst"]

def getInGroup(list):

    for i in range(0, len(list)):
        if i%4 == 0:
            print(namesList[i] + " is in group 1")
        elif i%4 == 1:
            print(namesList[i] + " is in group 2")
        elif i%4 == 2:
            print(namesList[i] + " is in group 3")
        elif i % 4 == 3:
            print(namesList[i] + " is in group 4")

print(getInGroup(namesList))



