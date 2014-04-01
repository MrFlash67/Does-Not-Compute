import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions
#class Parseable(object):
	#"""docstring for parseable"""
	#def __init__(self, parse):
	#	self.parse = parse
		#print 'Is This Broken 1.0'
		#print self.parse
	#def test(self):
	#	print 'This is hard, man!'
	#def parseInput(self):
		#print 'Is This Broken 1.1'
	#	return self.parse


def gameloop(invi):
	while True:
		command = string.lower(raw_input('> '))
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
		elif command == 'look around':
			pass
		elif command == 'quit':
			DoesNotComputeFunctions.exit()
		elif 'go' in command:
			pass
		elif 'take' in command:
			pass
		elif command == 'save':
			pass
		elif command == 'load':
			pass
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
		elif command == 'use':
			pass
		else:
			print 'Nope!'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz)