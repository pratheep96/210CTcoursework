initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
finalNumberList=[]
count = 0
temp = 0
while initialnumberList != finalNumberList:
    count = 0
    finalNumberList = initialnumberList
    print(initialnumberList)
    while count < (len(initialnumberList)-1):
        if initialnumberList[count] <= initialnumberList[count+1]:
            count = count + 1
        else:
            temp = initialnumberList[count]
            initialnumberList[count] = initialnumberList[count+1]
            initialnumberList[count+1] = temp
            count = count + 1
    print(initialnumberList)

    


        
        
