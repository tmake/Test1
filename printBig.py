from letters import Letters

def printBig(text, space=2):
	for line in range(len(Letters['a'])):
		lout = ""
		for ch in text:
			lout += Letters[ch][line]+" "*space
		print lout

