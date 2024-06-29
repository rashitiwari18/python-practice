import time
a = " hello world"
b= "abcdefghijklmnopqrstuvwxyz"
k= ""
for i in a:
     for j in b:
          print(k, end="")
          print(j)
          time.sleep(.05)
          if ( i==j ):
               k +=j
               break
     
     