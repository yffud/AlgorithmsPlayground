# implementation of bubble sort in Python.
# note python allows a shortcut without using a temporary variable during the assignments

def bubbleSort(someList):
	for runNumber in range(len(someList)-1,0,-1):
		# we are going to step backwards through the list
		# range(start, stop[, step])
		for index in range(runNumber):
			if someList[index]>someList[index + 1]:
				tempValue = someList[index]
				someList[index] = someList[index + 1]
				someList[index + 1] = tempValue




# setup a list 
someList = [32,12,54,98,23,10,4,102,64,78]

# run bubble sort
bubbleSort(someList)

#print the sorted list
print(someList)
