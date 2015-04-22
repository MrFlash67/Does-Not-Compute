import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions, DoesNotComputeMovement
from DoesNotComputeLocations import *
def countAdd(loopNum):
	loopNum = loopNum + 1
	return loopNum
def look(loc):
	DoesNotComputeFunctions.look(loc)
	DoesNotComputeFunctions.whichWays(locs[loc])
	if locs[loc].getLocType() == 'BlockedLocation':
		if not locs[loc].getIsOpen:
			print 'You can move through here'
		else:
			print 'You cannot move through here'
def gameloop(invi, loopNum):
	'''Main game loop'''
	nowLoc = 0
	while True:
		command = string.lower(raw_input('> '))
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
			pass
			#loopNum = countAdd(loopNum)
		elif command == 'load':
			pass
			#loopNum = countAdd(loopNum)
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
		elif command in ('go n', 'go north', 'n', 'move n'):
			nowLoc = DoesNotComputeMovement.goNorth(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go s', 'go south', 's', 'move s'):
			nowLoc = DoesNotComputeMovement.goSouth(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go w', 'go west', 'w', 'move w'):
			nowLoc = DoesNotComputeMovement.goWest(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command in ('go e', 'go east', 'e', 'move e'):
			nowLoc = DoesNotComputeMovement.goEast(nowLoc)
			look(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'open':
			DoesNotComputeFunctions.getIsOpen(nowLoc)
			DoesNotComputeFunctions.lockedOpen(nowLoc, invi)
			DoesNotComputeFunctions.getIsOpen(nowLoc)
			loopNum = countAdd(loopNum)
		elif command == 'loopn':
			print loopNum
		elif command == 'stop':
			print 'You stop and admire the view'
			loopNum = countAdd(loopNum)
		elif command == "exits":
			DoesNotComputeFunctions.whichWays(locs[nowLoc])
		elif command == 'items' or command == 'ii':
			DoesNotComputeFunctions.itemInfo(nowLoc)
		elif command == 'take':
			if DoesNotComputeFunctions.itemTF(nowLoc):
				if locs[nowLoc].getHasItems():
					invi.extend(DoesNotComputeFunctions.itemPickup(nowLoc))
					locs[nowLoc].swapItems()
				else:
					print 'You have already took all the items in this area.'
			else:
				print 'There are no items in this location.'
			loopNum = countAdd(loopNum)
		elif command == 'qopen':
			DoesNotComputeFunctions.getIsOpen(nowLoc)
		elif command == 'unlocked':
			if locs[nowLoc].getLocType() == 'BlockedLocation':
				print str(locs[nowLoc].whereCanGoUnlocked)
		elif command == 'get ye flask':
			print 'Ye can\'t get ye flask!'
		else:
			print 'Illegal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)