task=input("Do you want to code or decode?")
if task=="code":
  a=input("enter the word:")
  if len(a)<3 :
    print("code word is:",a[::-1])
  else:
    f=input("enter three random character at to append at the  starting:")
    l=input("enter three random character at to append at the ending:")
    b=a[0]
    g=a[1:]
    m=g+b
    coded=f+m+l
    print("code word is:",coded)
elif task == "decode":
  print("we will decode the word")
  a=input("enter the word to decode:")
  if len(a)<3 :
     print("the decoded word is:",a[::-1])
  else:
    f=a[3:-3]
    l=f[-1]
    g=f[:-1]
    decoded=l+g
    print("the decoded word is:",decoded)
else:
  print("Invalid input.Please type code or decode")
   