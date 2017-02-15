"""
interpreter.py --  This is were all of our code for the interpreter will go
"""
import sys
code = open(sys.argv[1], "r")\
.read()\
.split("\n")
myvars = {}
def tokenize(code):
	for line in code:
		tokens = line.split(" ", maxsplit=1)
		run(tokens) # we will define run next
def run(tokens):
	funcmap = {"MAKE": MAKE, "SET": SET, "PRINT": PRINT}
	try:
		funcmap[tokens[0]](tokens[1])
	except:
		raise SyntaxError("Cannot run command")
def MAKE(args):
	global myvars
	if myvars:
		myvars[args] = None
	else:
		myvars = {args: None}
def SET(arg): # the only data type is a string
	args = arg.split(",")
	global myvars
	if myvars:
		try:
			print(myvars[args[0]], file=open("LOG", "a"))
			myvars[args[0]] = args[1]
		except:
			raise NameError
	else:
		raise NameError
def PRINT(args):
	print(myvars[args])
if __name__ == "__main__":
  tokenize(code)
