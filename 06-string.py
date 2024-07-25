name = "rashi"
friend = " tiwari "
convo = ''' she said 
         hello rashi
         how are you
         i want to eat momos '''

# print("hello, " +name)
# print("conversation between us was: \n" +convo)

print(name[0])  # indexing position 1
print(name[1])  # indexing position 2
print(name[2])  # indexing position 3
print(name[3])  # indexing position 4
print(name[4])  # indexing position 5
print(name[5])  # throws an error bcoz position 6 does not exist

print(" let's use for loop ")
for character in convo:
    print(character)
