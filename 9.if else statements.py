# If- else statement example:--

price = int( input( " Enter price of apples"))
budget = 200
print(" Price of apples are: ", price)
print(" My budget is: ", budget)

if (budget > price):
    print(" Alexa, add 1kg apple to the cart ")
else:
    print(" Alexa, do not add apples to the cart")
print(" Keep shopping !!")  

# If- elif statement example:--

price = int( input( " Enter price of apples"))
budget = 200
print(" Price of apples are: ", price)
print(" My budget is: ", budget)
if  (budget - price > 50):
 print(" Alexa, add 1kg apple to the cart")
elif (budget - price > 80):
    print(" It's ok you can consider adding apple to the cart")    
else:
