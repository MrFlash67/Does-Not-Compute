import sys, time, string, os, time, pickle as pck

'''Legacy stuff from old system: /\ New stuff: \/'''

activelocationNumber = '11'

def swapActiveLocation(toMoveTo):
	activelocationNumber = toMoveTo 
	activeLocation = locations[toMoveTo]

class Location(object):
	'''Class for the locations'''
	where = 0
	def __init__(self, where, desc, whereCanGo, name, specialFeatures):
		self.where = where
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
	
	def getDesc(self):
		'''Get the description for the area'''
		return self.desc
	
	def whereIsIt(self):
		'''Find out its location in a integer.'''
		return self.where
	
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
		print 'Going to ' + str(toMoveTo) + '!'
		swapActiveLocation(toMoveTo)
		
class MultipuleLocation(Location):
	'''Class for the first location. Requires repeated use of the 'go' command'''
	timesTried = 0
	def __init__(self, howMany, where, desc, whereCanGo, name, specialFeatures, funnyThings, leavingFunnyThing):
		self.howMany = int(howMany)
		self.where = where
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
		'''Get the description for the area'''
		return self.desc
	
	def whereIsIt(self):
		'''Find out its location in a integer.'''
		return self.where
	
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

class containerLocation(Location):
	'''Holds items'''
	
	def __init__(self, whatItems, where, desc, whereCanGo, name, specialFeatures):
		self.whatItems = whatItems
		self.where = where
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
	
	def whereIsIt(self):
		'''Find out its location in a integer.'''
		return self.where
	
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

class BlockedLocation(Location):
	def __init__(self, where, desc, whereCanGoNB, name, specialFeatures, whereCanGoB, itemNeeded):
		self.where = where
		self.desc = desc
		self.whereCanGoNB = whereCanGoNB
		self.name = name
		self.specialFeatures = specialFeatures
		self.whereCanGoB = whereCanGoB
		self.itemNeeded = itemNeeded

	def getDesc(self):
		'''Get the description for the area'''
		return self.desc
	
	def whereIsIt(self):
		'''Find out its location in a integer.'''
		return self.where
	
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

#class Player(object):
	#'''The class for all stuff related to the player'''
	#def __init__(self, inventoryStart):
	#    self.inventoryStart = inventoryStart
		#self.locationNumber = locationNumber

	def getCurrentInv(self, inv):
		return 'You search your pockets. They contain ' + listStuff(inv) + ', ' + listStuff(self.inventoryStart) + '.' #Somewhat broken

def getCurrentLocation():
	#print 'Oh hi there, if you can see this then it is probably a typo somewhere. F88k. (Find E001 or this line)'
	return activelocationNumber 
		

locations = [Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom'), MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', ['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.', 'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.'), containerLocation(['lol', 'wut'], 11, 'A place with items', (900, 67, 42, 1), 'Song of Time', 'I say lol, it contains items, derp')]


if __name__ == '__main__':
	'''This is a docstring.'''
	activeLocation = locations[1]
	#swapActiveLocation(11)
	#intro()
	#test = containerLocation(['lol', 'wut'], 11, 'A place with items', (900, 67, 42, 1), 'Song of Time', 'I say lol, it contains items, derp')
	inv = ['No tea']
	player = Player(['Even less tea', 'Seriously, why are you here?']) #Make serious
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

	

