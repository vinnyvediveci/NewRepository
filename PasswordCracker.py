

password = "gr34asdfgxasgewtruwth23456fghsrhbsrehb25645yhtrsnhgfnj2457gfshb"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def PasswordCracker (str):
    print("Finding...")
    characters = ""

    for s in alphabet:
        j = 0
        if str[j] == s:
             characters += str.__add__(str[j])
             j += 1

    print("Password found: " + characters[:100])

PasswordCracker(password)


import hashlib
import random


print(hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())

print(str(random.getrandbits(256)))