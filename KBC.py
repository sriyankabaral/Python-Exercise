
a="!!!Wellcome To KBC!!!"
b=a.center(50)
print(b)
a=["What is the capital city of Nepal?","What is the chemical symbol for water?","Solve the following equation for (x): (3x + 5 = 14).","Who wrote the play “Romeo and Juliet?","What is the largest planet in our solar system?"]                  
prize=0
b=[["a.Kathmandu"," b.Pokhara ","c.Chitwan","d.Butwal"],["a.02", "b.HCL", "c.H2O", "d.H02"],["a.3", "b.4", "c.0" ,"d.9"],["a.Stan Lee", "b.William Shakespeare", "c.Roald Dahl", "d.Rabindranath Tagore"],["a.Jupiter", "b.Mars", "c.Saturn", "d.Uranus"]]
d=["a","c","a","b","a"]                                                                       
for i in range(len(a)):
 print(i+1,".Your question is:",a[i])
 print(b[i])                                                                                              
 c=input("enter your answer:")
 if(c==d[i]):
  prize=prize+1000
  print("Correct answer!!")
 else:
  print("wrong answer")
  print("Right answer is:",d[i]) 
print("YOU WON",prize,"rupees")
   
   
