# levenshtein distance calculation

def levenshtein( string1 , string2):
	if len(string1) < len(string2):
		return levenshtein(string2 , string1)

	if len(string2) == 0:
		return len(string1)

	previous_row = range(len(string2) + 1)
	for index, char1 in enumerate(string1):
		current_row = [index + 1]
		for j, char2 in enumerate(string2):
			insertions = previous_row[j + 1] + 1
			deletions = current_row[j] + 1
			substitutions = previous_row[j] + (char1 != char2)
			current_row.append(min(insertions, deletions, substitutions))
		previous_row = current_row

	return previous_row[-1]


# test

print levenshtein("test","tests")
print levenshtein("dir","dr")
print levenshtein("test","testing")