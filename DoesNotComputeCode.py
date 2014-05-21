import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions
def countAdd(loopNum):
	loopNum = loopNum + 1
	return loopNum
def gameloop(invi, loopNum):
	'''Main game loop'''
	while True:
		command = string.lower(raw_input('> '))
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
			loopNum = countAdd(loopNum)
		elif command == 'look around':
			pass
			loopNum = countAdd(loopNum)
		elif command == 'quit':
			DoesNotComputeFunctions.exit()
		elif 'go' in command:
			loopNum = countAdd(loopNum)
		elif 'take' in command:
			pass
			loopNum = countAdd(loopNum)
		elif command == 'save':
			pass
			#loopNum = countAdd(loopNum)
		elif command == 'load':
			pass
			#loopNum = countAdd(loopNum)
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
			loopNum = countAdd(loopNum)
		elif command == 'use':
			pass
			loopNum = countAdd(loopNum)
		elif command == 'loopn':
			print loopNum
		elif command == 'stop':
			loopNum = countAdd(loopNum)
		else:
			print 'Illegal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)