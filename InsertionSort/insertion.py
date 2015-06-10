def insertionSort(someList):
	for index in range(1,len(someList)):

		currentValue = someList[index]
		currentPosition = index

		while currentPosition > 0 and someList[currentPosition - 1] > currentValue:
			someList[currentPosition]=someList[currentPosition - 1]
			currentPosition = currentPosition - 1

		someList[currentPosition]=currentValue

# setup a list 
someList = [32,12,54,98,23,10,4,102,64,78]

# run insertion sort
insertionSort(someList)

#print the sorted list
print(someList)
