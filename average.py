num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

def average(num1, num2):
    return (num1 + num2) / 2

avg = average(num1, num2)
print(f"The average of {num1} & {num2} is: {avg}")