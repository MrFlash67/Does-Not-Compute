import sys, time, DoesNotComputeClasses, DoesNotComputeMovement
from DoesNotComputeLocations import locs
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
	print 'You can now enter commands. Type \'help\' without the quotation marks and press \'enter\' for help'


def listStuff(l):
	'''For getting inventory. Not obsolete.'''
	text = 'nill'
	for s in l:
		if text == 'nill':
			text = str(s)
			#print text + '1'
		else:
			text = text + ', ' + str(s)
			#print text + '2'
		
	return str(text)



def showHelp():
	'''The help display.'''
	'''Uncomment lines when implimented'''
	print 'All commands are case-insensitive.'
	print 'HELP: Display help'
	#print 'LOOK: Get a description of your surrounds'
	#print 'GO: Move about in the world'
	#print 'SAVE: Saves and exits your game'
	#print 'LOAD: Loads your save'
	print 'QUIT: Exit the game'
	print 'I or INV or INVENTORY: Display your inventory. Stuff in brackets (like this) next to the listing is a shortcut.'
	#print 'TAKE: Take all the objects in the room'
	#print 'USE (COM): Use an item in your inventory. Use the shortcut listed in the inventory to use it.'
	print 'STOP: Stop and contemplate the view'  


def exit():
	'''Exits the program'''
	print 'Something funny!'
	sys.exit()


def printDesc():
	'''Gets the description of a location.'''
	print str(inUseLocation.getDesc())


def look(activeLocation):
	'''Doctype B'''
	print locs[activeLocation].getDesc()


def whichWays(loc):
	pass
if __name__ == '__main__':
	intro()
	inUseLocation = testLoc
	testLoc = DoesNotComputeClasses.Location(1, 'Some cool place that kills you', (0, 2), 'The Cool Death Trap', 'It kills you')
	printDesc()