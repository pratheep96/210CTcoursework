#This is the given number list
initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
#For each element in the list the for loop is implemented n number of times
for i in range( 1, len(initialnumberList) ):
    temp = initialnumberList[i]
    x = i
    #This while loops sorts the numbers out in ascending order
    while x > 0 and temp < initialnumberList[x - 1]:
        initialnumberList[x] = initialnumberList[x - 1]
        x = x - 1
    initialnumberList[x] = temp
    #This prints the numbers in ascending order
    print(initialnumberList)
