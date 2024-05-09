num1=int(input("enter the first number="))
sign=input("+,-,*,/=")
num2=int(input("enter the second number="))

match sign:
    case '+':
     result=num1+num2
    case '-':
     result=num1-num2
    case '*':
     result=num1*num2
    case '/':
     result=num1/num2
    case "_":
        print("wrong input")
    
print("result of two number is=", result)
