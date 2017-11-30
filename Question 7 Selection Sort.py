#This is the given number list
initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]

#This for loops sorts the numbers in ascending order
for i in range(len(initialnumberList)):
    minimum = min(initialnumberList[i:])
    minimumIndex = initialnumberList[i:].index(minimum) 
    initialnumberList[i + minimumIndex] = initialnumberList[i] 
    initialnumberList[i] = minimum
    #This prints the numbers in ascending order    
    print (initialnumberList)

