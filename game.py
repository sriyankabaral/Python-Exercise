print("Hey ,Enjoy Snake Water Gun Game.\n ")
info=('snake','water','gun')
l=input(f"enter your choices:{info}\n")
items=random.choice(info)
print("The choice of opponent is:",items)
if(l==items):
 print("Its's a draw!!")
elif(l=='snake' and items=='water'):
    print('You won!!')
elif(l=='snake' and items=='gun' ):
    print('You lose!!')
elif(l=='water'and items=='snake'):
    print('You lose!!')
elif(l=='water'and items=='gun'):
    print('You won!!')
elif(l=='gun'and  items=='snake'):
    print('You won!!')
else:
  print('You lose!!')

