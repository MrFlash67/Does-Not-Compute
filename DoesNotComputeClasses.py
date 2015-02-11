import time, string, os

activelocationNumber = '11'

def swapActiveLocation(toMoveTo):
	'''Swaps active location'''
	activelocationNumber = toMoveTo 
	activeLocation = locations[toMoveTo]

class Location(object):
	'''Class for the locations'''
	locID = 0
	def __init__(self, locID, desc, whereCanGo, name, specialFeatures):
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
	
	def getDesc(self):
		'''Get the description for the area'''
		return self.desc
	
	def getNumLocation(self):
		'''Find out its location in a integer.'''
		return self.locID
	
	def whereCanGo(self):
		'''Return a tuple of the integer locations that the player can go to.'''
		return self.whereCanGo #Do NOT put in a print statement without doing some magic formatting!!!
		#And yes, I am insane.
	
	def getName(self):
		'''Get a string name of the location'''
		return self.name
		
	def getSpecialFeatures(self):
		'''Get the special features and attributes of a location in a string. Has no use in actual programming'''
		return self.specialFeatures
	
	def moveTo(self, toMoveTo):
		'''Swaps the active location'''
		swapActiveLocation(toMoveTo)

	def getLocType(self):
		return 'Location'
		
'''class MultipuleLocation(Location):
	'Class for the first location. Requires repeated use of the 'go' command'
	timesTried = 0
	def __init__(self, howMany, locID, desc, whereCanGo, name, specialFeatures, funnyThings, leavingFunnyThing):
		self.howMany = int(howMany)
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.funnyThings = funnyThings
		self.leavingFunnyThing = leavingFunnyThing
		self.timesTried = 0
		
	def moveTo(self, toMoveTo):
		toMoveTo = int(toMoveTo)
		if self.timesTried <= self.howMany: #if timesTried is equal to or above howMany, go to if, else go to else.
			#print 'Something witty!'
			#print self.timesTried
			print self.funnyThings[self.timesTried]
			self.timesTried += 1
			#print self.timesTried
		else:
			print self.leavingFunnyThing
			super(MultipuleLocation, self).moveTo(toMoveTo)
	
	def getDesc(self):
		Get the description for the area'
		return self.desc
	
	def getNumLocation(self):
		Find out its location in a integer.'
		return self.locID
	
	def whereCanGo(self):
		Return a tuple of the integer locations that the player can go to.'
		return self.whereCanGo #Do NOT put in a print statement without doing some magic formatting!!!
								#And yes, I am insane.
	
	def getName(self):
		'Get a string name of the location'
		return self.name
		
	def getSpecialFeatures(self):
		Get the special features and attributes of a location in a string. Has no use in actual programming'
		return self.specialFeatures

	def getLocType(self):
		return 'MultipuleLocation' '''

class containerLocation(Location):
	'''Holds items'''
	
	def __init__(self, whatItems, locID, desc, whereCanGo, name, specialFeatures):
		self.whatItems = whatItems
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures

	def moveTo(self, toMoveTo):
		super(containerLocation, self).moveTo(toMoveTo)

	def getItems(self):
		'''Get a list of the items here'''
		return self.whatItems#Do NOT put in a print statement without doing some magic formatting!!!
								#And yes, I am insane.
	
	def getDesc(self):
		'''Get the description for the area'''
		return self.desc
	
	def getNumLocation(self):
		'''Find out its location in a integer.'''
		return self.locID
	
	def whereCanGo(self):
		'''Return a tuple of the integer locations that the player can go to.'''
		return self.whereCanGo #Do NOT put in a print statement without doing some magic formatting!!!
								#And yes, I am insane.
	
	def getName(self):
		'''Get a string name of the location'''
		return self.name
		
	def getSpecialFeatures(self):
		'''Get the special features and attributes of a location in a string. Has no use in actual programming'''
		return self.specialFeatures

	def getLocType(self):
		return 'containerLocation'

class BlockedLocation(Location):
	def __init__(self, locID, desc, whereCanGo, name, specialFeatures, whereCanGoB, itemNeeded):
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.whereCanGoB = whereCanGoB
		self.itemNeeded = itemNeeded
		self.open = False

	def getDesc(self):
		'Get the description for the area'
		return self.desc
	
	def getNumLocation(self):
		'Find out its location in a integer.'
		return self.locID
	
	def whereCanGo(self):
		'Return a tuple of the integer locations that the player can go to.'
		return self.whereCanGo #Do NOT put in a print statement without doing some magic formatting!!!
		#And yes, I am insane.
	
	def getName(self):
		'Get a string name of the location'
		return self.name
		
	def getSpecialFeatures(self):
		'Get the special features and attributes of a location in a string. Has no use in actual programming'
		return self.specialFeatures
	def whatItemNeeded(self):
		'Returns the item needed to progress'
		return str(self.itemNeeded)
	def makeOpen(self):
		'Unlocks the BlockedLocation'
		if invi in (self.itemNeeded):
			self.open = True
	def getLocType(self):
		return 'BlockedLocation'

class BossLocation(Location): #All below TBI
	'''Class for the boss'''
	locID = 0
	def __init__(self, locID, desc, whereCanGo, name, specialFeatures, bossName, startTurn):
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.bossName = bossName
		self.startTurn = startTurn
	
	def getDesc(self):
		'''Get the description for the area'''
		return self.desc + "\nIt contains a massive monster called " + self.bossName + " who wants to kill you.\nGood luck."
	
	def getNumLocation(self):
		'''Find out its location in a integer.'''
		return self.locID
	
	def whereCanGo(self):
		'''Return a tuple of the integer locations that the player can go to.'''
		return self.whereCanGo #Do NOT put in a print statement without doing some magic formatting!!!
		#And yes, I am insane.
	
	def getName(self):
		'''Get a string name of the location'''
		return self.name
		
	def getSpecialFeatures(self):
		'''Get the special features and attributes of a location in a string. Has no use in actual programming'''
		return self.specialFeatures
	def attack(self, turn):
		if turn == self.startTurn or turn == self.startTurn + 1:
			return 'He attacks.\nHealth:\ninfinity/infinity\nFeel like waiting?'
		elif turn == self.startTurn + 2:
			return 'He dies from Sudden Death Syndrome.\nYou win.'
		else:
			return 'You broke it!'
	def getLocType(self):
		return 'BossLocation'
		

#class Player(object):
	#'''The class for all stuff related to the player'''
	#def __init__(self, inventoryStart):
	#    self.inventoryStart = inventoryStart
		#self.locationNumber = locationNumber

	def getCurrentInv(self, inv):
		return 'You search your pockets. They contain ' + listStuff(inv) + ', ' + listStuff(self.inventoryStart) + '.' #Somewhat broken

def getCurrentLocation():
	'''Gets current location'''
	#print 'Oh hi there, if you can see this then it is probably a typo somelocID. F88k. (Find E001 or this line)'
	return activelocationNumber 
		

#locations = [Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom'), MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', ['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.', 'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.'), containerLocation(['lol', 'wut'], 11, 'A place with items', (900, 67, 42, 1), 'Song of Time', 'I say lol, it contains items, derp')]


if __name__ == '__main__':
	'''This is a docstring.'''
	activeLocation = locations[1]
	#swapActiveLocation(11)
	#intro()
	#test = containerLocation(['lol', 'wut'], 11, 'A place with items', (900, 67, 42, 1), 'Song of Time', 'I say lol, it contains items, derp')
	inv = ['No tea']
	#player = Player(['Even less tea', 'Seriously, why are you here?']) #Make serious
	#print player.getCurrentInv(inv)
	#preBoss = Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom')
	#something = MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', ['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.', 'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.')
	print activeLocation.getDesc()
	print getCurrentLocation()
	print activeLocation.getSpecialFeatures()
	stuff = 0
	while stuff < 5:
		activeLocation.moveTo(1)
		stuff += 1
	print 'Demo mode over'''