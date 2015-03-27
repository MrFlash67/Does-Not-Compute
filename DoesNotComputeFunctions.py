import sys, time, DoesNotComputeMovement, DoesNotComputeClasses, DoesNotComputeLocations
#inUseLocation = DoesNotComputeClasses.getCurrentLocation()
def intro():
	'''Starts the program'''
	print 'MrFlash67 presents:'
	time.sleep(3)
	print '''
______                  _   _       _     _____                             _       
|  _  \                | \ | |     | |   /  __ \                           | |      
| | | |___   ___  ___  |  \| | ___ | |_  | /  \/ ___  _ __ ___  _ __  _   _| |_ ___ 
| | | / _ \ / _ \/ __| | . ` |/ _ \| __| | |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \\
| |/ / (_) |  __/\__ \ | |\  | (_) | |_  | \__/\ (_) | | | | | | |_) | |_| | ||  __/
|___/ \___/ \___||___/ \_| \_/\___/ \__|  \____/\___/|_| |_| |_| .__/ \__,_|\__\___|
							       | |
							       |_|
'''
	print
	print 'Press enter to continue.',
	raw_input()
	look(0)
	whichWays(DoesNotComputeLocations.locs[0])
	print 'You can now enter commands. Type \'help\' without the quotation marks and press \'enter\' for help'


def listStuff(l):
	'''For getting inventory. Not obsolete.'''
	text = 'nill'
	for s in l:
		if text == 'nill':
			text = str(s)
			#print text + '1'
		else:
			text = text + ' and a ' + str(s)
			#print text + '2'
		
	return str(text)

def showHelp():
	'''The help display.'''
	'''Uncomment lines when implimented'''
	print 'All commands are case-insensitive.'
	print 'HELP: Display help'
	print 'LOOK: Get a description of your surroundings'
	print 'GO n/s/e/w: Move about in the world'
	#print 'SAVE: Saves and exits your game'
	#print 'LOAD: Loads your save'
	print 'QUIT: Exit the game'
	print 'I or INV or INVENTORY: Display your inventory. Stuff in brackets (like this) next to the listing is a shortcut.'
	print 'TAKE: Take all the objects in the room'
	#print 'OPEN: Opens a door/blocked location if you have the required item.'
	print 'STOP: Stop and contemplate the view'  


def exit():
	'''Exits the program'''
	print 'Something funny!'
	sys.exit()


def printDesc():
	'''Gets the description of a location.'''
	print str(inUseLocation.getDesc())


def look(activeLocation):
	'''Observes the surroundings'''
	print DoesNotComputeLocations.locs[activeLocation].getDesc()


def whichWays(loc):
	loc0 = loc.whereCanGo[0]
	loc1 = loc.whereCanGo[1]
	loc2 = loc.whereCanGo[2]
	loc3 = loc.whereCanGo[3]
	loc = [loc0, loc1, loc2, locs]
	num = 0
	for loc in loc:
		if num == 0:
			way = 'North'
		elif num == 1:
			way = 'East'
		elif num == 2:
			way = 'South'
		elif num == 3:
			way = 'West'
		if loc == -1:
			print 'No moving to the {}!'.format(way)
		else:
			print 'You can go to the {}!'.format(way)
		#print num
		num = num + 1
		#print num

def itemInfo(loc):
	if DoesNotComputeLocations.locs[loc].getLocType() == 'containerLocation' and DoesNotComputeLocations.locs[loc].getHasItems():
		print 'There is ' + listStuff(DoesNotComputeLocations.locs[loc].getItems()) + ' lying on the floor.'
	else:
		print 'There are no items in this location.'

def itemTF(loc):
	if DoesNotComputeLocations.locs[loc].getLocType() == 'containerLocation':
		return True
	else:
		return False

def itemPickup(loc):
	try:
		print 'You now have ' + listStuff(DoesNotComputeLocations.locs[loc].getItems()) + ' in your inventory.'
		return DoesNotComputeLocations.locs[loc].getItems()
	except TypeError:
		print 'There are no items in this location.'
		return None
	except AttributeError:
		print 'There are no items in this location.'
		return None

def lockedOpen(loc, neededItem):
	if DoesNotComputeLocations.locs[loc].getLocType() == 'blockedLocation':
		if not DoesNotComputeLocations.locs[loc].getIsOpen():
			if DoesNotComputeLocations.locs[loc].
		else:
			print 'The door is already open.'
	else:
		print 'There is nothing to unlock in this location'


if __name__ == '__main__':
	whichWays([-1, 2, -1, 3])