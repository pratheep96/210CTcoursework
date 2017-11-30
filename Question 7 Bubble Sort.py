#This is the given number list
initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
#This is a loop that sorts the numbers into ascending order based where they are in the list
count = len(initialnumberList)-1
while count > 0:
    for i in range(0,count):
        if initialnumberList[i]>=initialnumberList[i+1]:
            initialnumberList[i], initialnumberList[i+1] = initialnumberList[i+1], initialnumberList[i]
    count = count - 1
    #This prints the numbers in ascending order
    print(initialnumberList)    


        
        
