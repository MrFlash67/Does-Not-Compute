import sys, DoesNotComputeClasses, string, DoesNotComputeFunctions, DoesNotComputeMovement, fnmatch
from DoesNotComputeLocations import *
def countAdd(loopNum):
	loopNum = loopNum + 1
	return loopNum
def gameloop(invi, loopNum):
	'''Main game loop'''
	nowLoc = 0
	help = 0
	while True:
		if help > 4:
			print 'Need any help?\nYou can always use the \'help\' command!'
			help = 0
		command = string.lower(raw_input('> '))
		if command == 'help':
			DoesNotComputeFunctions.showHelp()
			loopNum = countAdd(loopNum)
			help = 0
		elif command == 'look':
			DoesNotComputeFunctions.look(loc)
			DoesNotComputeFunctions.whichWays(locs[loc])
			if locs[loc].getLocType() in ('BlockedLocation', 'BossLocation'):
				if locs[loc].getIsOpen():
					print 'There is an unlocked door or fixed obstacle here.'
				else:
					print 'There is a locked door or obstacle here.'
			help += 1
		elif command == 'go':
			print 'Use "go north/south/east/west/n/s/e/w"'
		elif command in ('quit', 'exit', 'leave'):
			DoesNotComputeFunctions.exit()
		elif command == 'save':
			DoesNotComputeFunctions.save(DoesNotComputeFunctions.getInfo(nowLoc, invi, loopNum))
		elif command == 'load':
			if DoesNotComputeFunctions.load():
				info = DoesNotComputeFunctions.load()
				nowLoc = info[0]['location']
				invi = info[0]['inventory']
				loopNum = info[0]['loopNum']
				print 'Data loaded'
		elif command in ('inv', 'i', 'inventory'):
			print 'Your inventory contains: ' + DoesNotComputeFunctions.listStuff(invi)
			help += 1
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
			if DoesNotComputeFunctions.getIsOpen(nowLoc):
				help -=1
			else:
				help +=1 
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
					help -= 1
				else:
					print 'You have already taken all the items in this area.'
					help += 1
			else:
				print 'There are no items in this location.'
				help +=1
			loopNum = countAdd(loopNum)
		elif command == 'get ye flask':
			print 'Ye can\'t get ye flask!'
		elif command == 'helpa':
			print help
		elif command == 'attack' or command == 'fight':
			DoesNotComputeFunctions.attack(nowLoc, loopNum)
			loopNum = countAdd(loopNum)
		elif fnmatch.fnmatch(command, 'take *') or fnmatch.fnmatch(command, 'get *') or fnmatch.fnmatch(command, 'use *') or fnmatch.fnmatch(command, 'open* ') or fnmatch.fnmatch(command, 'unlock *'):
			print 'You do not need to specify an argument for that command.'
		else:
			print 'Illegal command.\nYou will be arrested posthaste.'
if __name__ == '__main__':
	stuffz = ['bob', 'bill']
	gameloop(stuffz, 0)