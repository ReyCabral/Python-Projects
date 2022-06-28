
from ntpath import join
from random import randint

listNumbers = []
i = 1 

def isValid(numberToGenerate):

    if numberToGenerate.strip().isdigit():
        if(int(numberToGenerate) <= 0):
            return True
        elif(int(numberToGenerate) > 25):
            return True
        else:
            return False       
    else:     
        return True
        
        
def sumListNumber(listNumbers):
    sum=0
    for number in listNumbers:
        sum += number
    return sum    


print("How many numbers would you like the program to generate?")
numberToGenerate = input()


while isValid(numberToGenerate):
    print("")
    print("The program is expectingenter an integer number greater than 0 and less or equal to 25. Please enter a valid value:")
    numberToGenerate = input()


while i <= int(numberToGenerate):
    number = randint(1,100)
    i += 1
    listNumbers.append(number)
    

print("")
print("The generated numbers are: ", *listNumbers)
print("The sum of the even numbers is: ", sumListNumber(listNumbers))