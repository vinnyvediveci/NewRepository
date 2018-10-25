import os
try:
    #raise NameError
    os.makedirs("C:/")
except PermissionError as error:

#runs if error # except PermissionError as error:
    print("Error caught", error)

else:                                #runs if no error
    print("it works")

#finally:
 #runs everytime
  #  file.close()


try:
    3 / 0
except ZeroDivisionError as error:
    print("error caught", error)

else:
    print("Mathematicians are wrong")


try:
    assert True == False, "Logic break"
except AssertionError as error:
    print("Error caught", error)
else:
    print("It works")

dictionary = dict()
dictionary["Key"] = "Value"

try:
  this = dictionary["false key"]
except KeyError as error:
    print("Error caught", error)
else:
    print("no key there")

try:
    os.makedirs("werter")
except WindowsError as error:
    print("Error caught", error)
else:
    print("it works")

try:
    dictionary = dict()
    dictionary["Key"] = "Value"
except SyntaxError as error:
    print("Error caught", error)
else:
    print("Great")

try:
    import ypmammp
except BaseException as error:
    print("Error caught", error)
else:
    print("great")


try:
    for i in range(0, 2):
        print("num")
except IndentationError as error:
    print("Error caught", error)
else:
    print("great")

try:
    os.listdir("waeratr")
except FileNotFoundError as error:
    print("Error caught", error)
else:
    print("great")




