import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions
def gameloop(invi, loopNum):
	'''Main game loop'''
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
		return loopNum
		loopNum = loopNum + 1

if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz)