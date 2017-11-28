initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]

for i in range(len(initialnumberList)):
    minimum = min(initialnumberList[i:])
    minimumIndex = initialnumberList[i:].index(minimum) 
    initialnumberList[i + minimumIndex] = initialnumberList[i] 
    initialnumberList[i] = minimum
    print (initialnumberList)

