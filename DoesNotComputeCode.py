import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions, DoesNotComputeMovement, fnmatch
from DoesNotComputeLocations import *
def countAdd(loopNum):
	loopNum = loopNum + 1
	return loopNum
def look(loc):
	DoesNotComputeFunctions.look(loc)
	DoesNotComputeFunctions.whichWays(locs[loc])
	if locs[loc].getLocType() in ('BlockedLocation', 'BossLocation'):
		if locs[loc].getIsOpen():
			print 'You can move through here'
		else:
			print 'You cannot move through here'
def gameloop(invi, loopNum):
	'''Main game loop'''
	nowLoc = 0
	while True:
		command = raw_input('> ')
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
			loopNum = countAdd(loopNum)
		elif command == 'look':
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'go':
			print 'Use "go north/south/east/west/n/s/e/w"'
		elif command in ('quit', 'exit', 'leave'):
			DoesNotComputeFunctions.exit()
		elif command == 'save':
			print 'You cannot save in this version.\nDownload a different version from mrflash67.github.io/Does-Not-Compute'
		elif command == 'load':
			print 'You cannot save in this version.\nDownload a different version from mrflash67.github.io/Does-Not-Compute'
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
		elif command in ('north', 'go n', 'go north', 'n', 'move n', 'move north'):
			nowLoc = DoesNotComputeMovement.goNorth(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('south', 'go s', 'go south', 's', 'move s', 'move south'):
			nowLoc = DoesNotComputeMovement.goSouth(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('west', 'go w', 'go west', 'w', 'move w', 'move west'):
			nowLoc = DoesNotComputeMovement.goWest(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('east', 'go e', 'go east', 'e', 'move e', 'move east'):
			nowLoc = DoesNotComputeMovement.goEast(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('open', 'use', 'unlock'):
			DoesNotComputeFunctions.getIsOpen(nowLoc)
			DoesNotComputeFunctions.lockedOpen(nowLoc, invi)
			DoesNotComputeFunctions.getIsOpen(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'loopn':
			print loopNum
		elif command in ('stop', 'wait'):
			print 'You stop and admire the view'
			loopNum = countAdd(loopNum)
		elif command == "exits":
			DoesNotComputeFunctions.whichWays(locs[nowLoc])
		elif command == 'items' or command == 'ii':
			DoesNotComputeFunctions.itemInfo(nowLoc)
		elif command in ('take', 'get', 'take all'):
			if DoesNotComputeFunctions.itemTF(nowLoc):
				if locs[nowLoc].getHasItems():
					invi.extend(DoesNotComputeFunctions.itemPickup(nowLoc))
					locs[nowLoc].swapItems()
				else:
					print 'You have already taken all the items in this area.'
			else:
				print 'There are no items in this location.'
			loopNum = countAdd(loopNum)
		elif command == 'get ye flask':
			print 'Ye can\'t get ye flask!'
		elif command == 'attack' or command == 'fight':
			DoesNotComputeFunctions.attack(nowLoc, loopNum)
		elif fnmatch.fnmatch(command, 'take *') or fnmatch.fnmatch(command, 'get *') or fnmatch.fnmatch(command, 'use *') or fnmatch.fnmatch(command, 'open* ') or fnmatch.fnmatch(command, 'unlock *'):
			print 'You do not need to specify an argument for that command.'
		else:
			print 'Illegal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)