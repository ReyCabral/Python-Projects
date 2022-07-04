
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

    userChoiceOperation = input("Enter your choice (1, 2, 3 or 4): ")
    if int(userChoiceOperation) < 5:

        userChoiceNum1 = float(input("Enter first number: "))
        userChoiceNum2 = float(input("Enter second number: "))

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

