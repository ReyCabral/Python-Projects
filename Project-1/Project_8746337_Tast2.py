
def add(num1,num2):
    return (num1 + num2)


def subtract(num1,num2):
    return (num1 - num2)


def multiply(num1,num2):
    return (num1 * num2)

def divide(num1,num2):
    return (num1 / num2)  


print("Select an operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    userChoiceNum1 = 0
    userChoiceNum2 = 0
    userChoiceOperation = input("Enter your choice (1, 2, 3 or 4): ")

    if userChoiceOperation in ('1', '2', '3', '4'):


        while True:
            try:
                userChoiceNum1 = float(input("Enter first number: "))      
            except ValueError:
                print("The program is expecting a numerical value")
                continue
            else:
                break 

        while True:
            try:
                userChoiceNum2 = float(input("Enter second number: "))      
            except ValueError:
                print("The program is expecting a numerical value")
                continue
            else:
                break 
        

        if userChoiceOperation == '1':
            print(userChoiceNum1, "+", userChoiceNum2, "=", "{:.2f}".format(add(userChoiceNum1, userChoiceNum2)))
            break

        elif userChoiceOperation == '2':
            print(userChoiceNum1, "-", userChoiceNum2, "=", "{:.2f}".format(subtract(userChoiceNum1, userChoiceNum2)))
            break

        elif userChoiceOperation == '3':
            print(userChoiceNum1, "*", userChoiceNum2, "=", "{:.2f}".format(multiply(userChoiceNum1, userChoiceNum2)))
            break

        elif userChoiceOperation == '4':
            print(userChoiceNum1, "/", userChoiceNum2, "=", "{:.2f}".format(divide(userChoiceNum1, userChoiceNum2)))
            break

    else:   

        print("Invalid Input") 
        




