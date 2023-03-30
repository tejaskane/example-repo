num=int(input("enter a number : "))
if (num%2==0):
    print(" {} is even.".format(num))
else:
    print(" {} is odd.".format(num))

print("now 2nd task")
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))

if num1>num2:
    print("{} is greater than {}.".format(num1,num2))
elif num2>num1:
    print("{} is greater than {}.".format(num2,num1))
else:
    print("{} is equal to {}.".format(num2,num1))
