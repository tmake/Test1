
Letters= {
"H":[	"H   H",
	"H   H",
	"H   H",
	"HHHHH",
	"H   H",
	"H   H",
	"H   H",],
"a": [	"     ",
	"     ",
	" aaa ",
	"    a",
	" aaaa",
	"a   a",
	" aaaa"],
"e": [	"     ",
	"     ",
	" eee ",
	"e   e",
	"eeeee",
	"e    ",
	" eeee"],
"l": [ 	"lll  ",
	" ll  ",
	" ll  ",
	" ll  ",
	" ll  ",
	" ll  ",
	"  lll"],
"o": [	"     ",
	"     ",
	" ooo ",
	"o   o",
	"o   o",
	"o   o",
	" ooo "],
"W": [	"W   W",
	"W   W",
	"W   W",
	"W W W",
	"W W W",
	" WWW ",
	" W W "],
"r": [	"     ",
	"     ",
	"rrrr ",
	"rr rr",
	"rr   ",
	"rr   ",
	"rr   ",],
"d":[	"    d",
	"    d",
	"    d",
	" dddd",
	"d   d",
	"d   d",
	" dddd"],
" ":["    " for i in range(8)]}



def printBig(text, space=2):
	for line in range(len(Letters['a'])+1):
		lout = ""
		for ch in text:
			lout += Letters[ch][line]+" "*space
		print lout


if __name__=="__main__":
	print "Test github and do some Python-stuff"
	printBig("Hello World")

	
