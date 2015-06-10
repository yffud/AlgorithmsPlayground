# implementation of selection sort in Python.

def selectionSort(someList):
	for slot in range(len(someList)-1,0,-1):
		# working bacwards
		positionOfMax=0
		# Find where the max value is
		for location in range(1,slot+1):
			if someList[location]>someList[positionOfMax]:
				positionOfMax = location

			# preform the swap of values
			tempValue = someList[slot]
			someList[slot] = someList[positionOfMax]
			someList[positionOfMax] = tempValue





# setup a list 
someList = [32,12,54,98,23,10,4,102,64,78]

# run bubble sort
selectionSort(someList)

#print the sorted list
print(someList)
