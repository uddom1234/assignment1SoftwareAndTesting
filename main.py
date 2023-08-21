def findVal(B):
   valArray = []


   for A in range(-100, 101):
       if (A + B == A - B) or (A * B == A - B) or (A / B == A - B): #this checks if a-b is equal to any possible alternative
           valArray.append(A) #if it does, then it appends to an array
       elif (A + 2 == A * 2) or (A - 2 == A * 2) or (A / 2 == A * 2):  #this checks if a*2 is equal to any possible alternative
           valArray.append(A)


   return valArray


B = 1

#this will produce the array of A values that are not detectable
notDetectableVal = findVal(B)
print(notDetectableVal)
