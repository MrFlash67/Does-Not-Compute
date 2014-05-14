import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions

def countAdd(loopNum):
	return loopNum
	loopNum = loopNum + 1


def gameloop(invi, loopNum):
	'''Main game loop'''
	while True:
		command = string.lower(raw_input('> '))
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
			countAdd(loopNum)
		elif command == 'look around':
			pass
			countAdd(loopNum)
		elif command == 'quit':
			DoesNotComputeFunctions.exit()
			
		elif 'go' in command:
			pass
			countAdd(loopNum)
		elif 'take' in command:
			pass
			countAdd(loopNum)
		elif command == 'save':
			pass
			#countAdd(loopNum)
		elif command == 'load':
			pass
			#countAdd(loopNum)
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
			countAdd(loopNum)
		elif command == 'use':
			pass
			countAdd(loopNum)
		elif command == 'loopn':
			print str(loopNum)
		else:
			print 'Illeagal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)