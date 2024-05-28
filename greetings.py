import time
t = time.strftime('%H:%M:%S')
print(t)

# Morning time zone starts at 04:00:00 to 11:59:59
# Afternoon time zone starts at 12:00:00 to 15:59:59
# Evening time zone starts at 16:00:00 to 19:59:59
# Night time zone starts at 20:00:00 to 24:59:59
name=input("enter your name:")
hrs=int(time.strftime('%H'))
if(hrs>= 4 and hrs<= 12):
 print ("goodmorning ",name)
elif (hrs >=12 and hrs <=16):
 print("goodafternoon",name)
elif (hrs >=16 and hrs <=20):
 print("goodevening",name)
else :
 print("goodnight",name)


