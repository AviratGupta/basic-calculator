print("---------------calculator---------------")
print("PRESS 1 TO ADD")
print("PRESS 2 TO SUBTRACT")
print("PRESS 3 TO MULTIPLY")
print("PRESS 4 TO DIVIDE")
choice = int(input())
if choice in (1,2,3,4):
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a number:"))
    if choice == 1:
        print("sum is = ",num1+num2)
    elif choice == 2:
        print("subtract is = ",num1-num2)
    elif choice == 3:
        print("multiply is = ",num1*num2)
    else:
        print("sum is = ",num1/num2)
else:
    print("entered option is unavailable")
print("---------------the end---------------")
