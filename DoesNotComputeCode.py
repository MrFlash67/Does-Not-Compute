import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions, DoesNotComputeMovement
def countAdd(loopNum):
	loopNum = loopNum + 1
	return loopNum
def gameloop(invi, loopNum):
	'''Main game loop'''
	nowLoc = 0
	while True:
		command = string.lower(raw_input('> '))
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
			loopNum = countAdd(loopNum)
		elif command == 'look':
			#pass
			DoesNotComputeFunctions.look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'go':
			print 'Use "go north/south/east/west/n/s/e/w"'
		elif command == 'quit':
			DoesNotComputeFunctions.exit()
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
		elif command in ('go n', 'go north', 'n'):
			nowLoc = DoesNotComputeMovement.goNorth(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go s', 'go south', 's'):
			nowLoc = DoesNotComputeMovement.goSouth(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go w', 'go west', 'w'):
			nowLoc = DoesNotComputeMovement.goWest(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go e', 'go east', 'e'):
			nowLoc = DoesNotComputeMovement.goEast(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'use':
			pass
			loopNum = countAdd(loopNum)
		elif command == 'loopn':
			print loopNum
		elif command == 'stop':
			print 'You stop and admire the view'
			loopNum = countAdd(loopNum)
		else:
			print 'Illegal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)