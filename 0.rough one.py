a = " hello world"
b= "abcdefghijklmnopqrstuvwxyz"
for i in a:
     for j in b:
          print(j, end=" ")
          if ( j == i):
              break
     
     