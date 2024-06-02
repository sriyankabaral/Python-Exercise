a="!!!Wellcome To KBC!!!"
c=a.center(50)
print(c)
a=["What is the capital city of Nepal?","What is the chemical symbol for water?","Solve the following equation for (x): (3x + 5 = 14).","Who wrote the play “Romeo and Juliet?","What is the largest planet in our solar system?"]
b=["Kathmandu","H2O","3","William Shakespeare","Jupiter"]
prize=0
for i in range(len(a)):
 print("Your question is:",a[i])
 c=input("enter your answer:")
 if(c==b[i]):
  prize=prize+1000
  print("Correct answer!!")
 else:
  print("wrong answer")
print("YOU WON",prize,"rupees")
   
