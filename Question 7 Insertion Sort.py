initialnumberList = [2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
for i in range( 1, len(initialnumberList) ):
    temp = initialnumberList[i]
    x = i
    while x > 0 and temp < initialnumberList[x - 1]:
        initialnumberList[x] = initialnumberList[x - 1]
        x = x - 1
    initialnumberList[x] = temp
    print(initialnumberList)
