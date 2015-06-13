def testConcat():
	someList = []
	for index in range(1000):
		someList = someList + [index]

def testAppend():
	someList = []
	for index in range(1000):
		someList.append(index)

def testCompression():
	someList = [i for i in range(1000)]

def testRange():
	someList = list(range(1000))

import timeit

time1 = Timer("testConcat","from __main__ import testConcat")
print("concat ",time1.timeit(number=1000), "milliseconds")

