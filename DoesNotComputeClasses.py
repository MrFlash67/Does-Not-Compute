import time, string, os, sys

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

	def getLocType(self):
		return 'Location'

class containerLocation(Location):
	'''Holds items'''
	
	def __init__(self, whatItems, locID, desc, whereCanGo, name, specialFeatures):
		self.whatItems = whatItems
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.hasItems = True

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

	def getHasItems(self):
		return self.hasItems

	def swapItems(self):
		self.hasItems = False

class BlockedLocation(Location):
	def __init__(self, locID, desc, whereCanGo, name, specialFeatures, whereCanGoUnlocked, itemNeeded):
		self.locID = locID
		self.desc = desc
		self.whereCanGo = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.whereCanGoUnlocked = whereCanGoUnlocked
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

	def whereCanGoUnlocked(self):
		return self.whereCanGoUnlocked
	
	def getName(self):
		'Get a string name of the location'
		return self.name
		
	def getSpecialFeatures(self):
		'Get the special features and attributes of a location in a string. Has no use in actual programming'
		return self.specialFeatures

	def getItemNeeded(self):
		'Returns the item needed to progress'
		return str(self.itemNeeded)

	def makeOpen(self):
		'Unlocks the BlockedLocation'
		self.open = True

	def getIsOpen(self):
		return self.open

	def getLocType(self):
		return 'BlockedLocation'

class BossLocation(Location): #All below TBI
	'''Class for the boss'''
	locID = 0
	def __init__(self, locID, desc, whereCanGo, name, specialFeatures, bossName):
		self.locID = locID
		self.desc = desc
		self.whereCanGo = [-1, -1 , -1, -1]
		self.whereCanGoUnlocked = whereCanGo
		self.name = name
		self.specialFeatures = specialFeatures
		self.bossName = bossName
		self.alive = True
		self.startTurn = 0
	
	def getDesc(self):
		'''Get the description for the area'''
		return self.desc + "\nIt contains a massive monster called " + self.bossName + " who wants to kill you.\nGood luck."
	
	def getNumLocation(self):
		'''Find out its location in a integer.'''
		return self.locID
	
	def whereCanGoUnlocked(self):
		'''Return a tuple of the integer locations that the player can go to.'''
		return self.whereCanGoUnlocked #Do NOT put in a print statement without doing some magic formatting!!!
		#And yes, I am insane.
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
		if self.startTurn == 0:
			self.startTurn = turn + 1
		if self.alive == True:
			if turn < self.startTurn:
				return 'He attacks.\nHealth:\ninfinity/infinity\nFeel like waiting?'
			elif turn >= self.startTurn:
				self.alive = False
				print 'He dies from Sudden Death Syndrome.\nYou win.\n\n'
				print 'You have won.\nWell done.\nYou have scored 1 million out of a possible 10 points.'
				#sys.exit()
			else:
				return 'You broke it!'
		else:
			print 'He\'s dead, Jim! You can stop bothering him, let him sleep'


	def getIsOpen(self):
		if self.alive:
			print 'alive'
			return False
		else:
			print 'not alive'
			return True
			

	def getLocType(self):
		return 'BossLocation'
