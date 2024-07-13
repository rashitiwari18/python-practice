# strings are immutable
a = " !! Rashi !!! "
print(a)
print(len(a))     # returns the length of the string

print(a.upper())  # converts lowercase to uppercase
print(a.lower())  # converts uppercase to lowercase
print(a.title())  # converts first alphabet of each letter capital

print(a.rstrip("!"))                    # removes only end drilling characters
print(a.replace("Rashi", "Tashu"))      # if there was more occurences all would have changed
print(a.split(" "))                     # splits wherever it gets " " as mentioned and converts it into list
