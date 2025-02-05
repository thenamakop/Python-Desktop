import string
import time
import random
def generator(target):
    letters = string.ascii_letters+" "
    result = ""
    for letter in target:
        while True:
            let = random.choice(letters)
            print(result+let)
            if(let==letter):
                result +=  let
                break
            time.sleep(0.01)

#main
x = input("Enter a wordyou want to generate: ")
generator(x)