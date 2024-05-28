g="*CALCULATOR*"
print(g.center(50))
l=input("enter the operation you want to perform:")
a=int(input("enter the first operand:"))
b=int(input("enter the second operand:"))

if(l=="+"):
 print("The value of", a, "+", b, "is: ", a + b)
elif(l=="-"):
 print("The value of", a, "-", b, "is: ", a - b)
elif(l=="*"):
 print("The value of", a, "*", b, "is: ", a * b)
elif(l=="/"):
 print("The value of", a, "/", b, "is: ", a / b)
elif(l=="%"):
 print("The value of", a, "%", b, "is: ", a % b)
elif(l=="**"):
 print("The value of", a, "**", b, "is: ", a ** b)
elif(l=="//"):
 print("The value of", a, "//", b, "is: ", a // b)
else:
 print("invalid operation")
