# implementation of selection sort in Python.

def selectionSort(someList):
	for slot in range(len(someList)-1,0,-1):
		# working bacwards
		# hold the index of the highest number
		indexOfMax=0
		# Find where the max value is
		for sortLocation in range(1,slot+1):
			if someList[sortLocation]>someList[indexOfMax]:
				indexOfMax = sortLocation

			# preform the swap of values
			tempValue = someList[slot]
			someList[slot] = someList[indexOfMax]
			someList[indexOfMax] = tempValue





# setup a list 
someList = [32,12,54,98,23,10,4,102,64,78]

# run bubble sort
selectionSort(someList)

#print the sorted list
print(someList)
