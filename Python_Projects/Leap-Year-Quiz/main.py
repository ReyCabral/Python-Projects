from random import randint


#variables to define the range of rondom years.
startYear = 1900
endYear = 2020
# goodQuestions variale that store the number of question that the user want
goodQuestions = 0
#variable i is iqual to 1 to start question for the number 1 not to cero. 
i = 1


#funtion to calculate if a year it is a Leap Year
def checkLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False



print("Hello, please enter your name: ")
name = input()
print('Welcome to the "Leap Year" Quiz, ' + str(name) + "!")
print("How many questions would you like to go with in the quiz? ")
numQuestion = input()
print("Ok, here we go!")
print("")

while i < int(numQuestion) + 1:
    year = randint(startYear,endYear)
    print(i,". Year " , str(year) , " is a leap year - True or False?")
    answer = input()
    if answer.upper() == "TRUE" and checkLeapYear(year):
        print("- Correct!")
        goodQuestions += 1
        print("")
    elif answer.upper() == "FALSE" and checkLeapYear(year) == False:
        print("- Correct!")
        goodQuestions += 1
        print("")
    else:
        print("- Incorrect answer.")    
    i += 1

print("")
print("You have completed the quiz. You've got", str(goodQuestions), "out of", str(i - 1), "questions correctly.")
