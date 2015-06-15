import sys, time, DoesNotComputeMovement, DoesNotComputeClasses, DoesNotComputeLocations
def intro():
	'''Starts the program'''
	print 'MrFlash67 presents:'
	time.sleep(2)
	print '''
  ___               _  _     _      ___                     _       
 |   \ ___ ___ ___ | \| |___| |_   / __|___ _ __  _ __ _  _| |_ ___ 
 | |) / _ / -_(_-< | .` / _ |  _| | (__/ _ | '  \| '_ | || |  _/ -_)
 |___/\___\___/__/ |_|\_\___/\__|  \___\___|_|_|_| .__/\_,_|\__\___|
                                                 |_|                
'''
	print
	print 'Press enter to continue.',
	raw_input()
	print
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
	print 'All commands are case-sensitive and should be entered in lowercase'
	print 'HELP: Display help'
	print 'LOOK: Get a description of your surroundings'
	print 'GO n/s/e/w: Move about in the world'
	print 'SAVE: Saves and exits your game'
	print 'LOAD: Loads your save'
	print 'QUIT: Exit the game'
	print 'I or INV or INVENTORY: Display your inventory.'
	print 'TAKE: Take all the objects in the room'
	print 'OPEN: Opens a door/blocked location if you have the required item'
	print 'STOP: Stop and contemplate the view'
	print 'ATTACK: Attack the nearby monster'  


def exit():
	'''Exits the program'''
	print 'Something funny!'
	sys.exit()


def look(activeLocation):
	'''Observes the surroundings'''
	print DoesNotComputeLocations.locs[activeLocation].getDesc()


def whichWays(loc):
	moveLocs = loc.whereCanGo
	loc0 = moveLocs[0]
	loc1 = moveLocs[1]
	loc2 = moveLocs[2]
	loc3 = moveLocs[3]
	loc = [loc0, loc1, loc2, loc3]
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

def lockedOpen(loc, inv):
	if DoesNotComputeLocations.locs[loc].getLocType() == 'BlockedLocation':
		if not DoesNotComputeLocations.locs[loc].getIsOpen():
			if  DoesNotComputeLocations.locs[loc].getItemNeeded() in inv:
				DoesNotComputeLocations.locs[loc].makeOpen()
				print 'You can now move through this door.'
			else:
				print 'You do not have the key need to open this door.'
		else:
			print 'The door is already open.'
	else:
		print 'There is nothing to unlock in this location'

def getIsOpen(loc):
		if DoesNotComputeLocations.locs[loc].getLocType() in ('BlockedLocation', 'BossLocation'):
			if DoesNotComputeLocations.locs[loc].getIsOpen():
				return True
			else:
				return False


def getInfo(loc, inventory, loopNum):
	locID = DoesNotComputeLocations.locs[loc].getLocID()
	return [{'location':locID, 'inventory':inventory, 'loopNum':loopNum}]

	
def attack(loc, turn):
	if DoesNotComputeLocations.locs[loc].getLocType() == 'BossLocation':
		print DoesNotComputeLocations.locs[loc].attack(turn)

if __name__ == '__main__':
	whichWays([-1, 2, -1, 3])