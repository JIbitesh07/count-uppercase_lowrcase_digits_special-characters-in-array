arr=str(input())
#assigning the variable with value "0" to count the number of uppercase,lowercase,characters and digits 
upper=0
lower=0
characters=0
digits=0
#using the for loop to iterate through the string input to count the number of uppercase,lowercase,characters and digits
for i in arr:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
        upper=upper+1
    elif(i>="0" and i<="9"):
        digits=digits+1
    else:
        characters=characters+1
#printing the number of elements
print("the number of upercase elements are",upper)
print("the number of lowercase numbers are",lower)
print("the number of characters are",characters)
print("the number of digits are",digits)


