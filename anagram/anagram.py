def anagramSolver(s1,s2):
	someList = list(s2)

	postion1 = 0
	stillGood = True

	while postion1 < len(s1) and stillGood:
		position2 = 0
		anagramFound = false
		while position2 < len(somelist) and not anagramFound:
			if s1[postion1] == somelist[position2]:
				anagramFound = True
			else:
				position2 = position2 + 1

		if anagramFound:
			somelist[position2] = None
		else:
			stillGood = false

		postion1 = postion1 + 1

	return stillGood


print(anagramSolver('dcba','abcd'))
