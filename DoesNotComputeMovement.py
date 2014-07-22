import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def getNum():
	
	wheretoGo = raw_input('Enter in the location number shown above\n> ')
	return wheretoGo
def isBorken(nowLocGo, locNum ,nowLocName, nowLocNum):
	fusRoDah = nowLocGo[0]
	#print nowLocGo[0]
	while locNum < len(nowLocGo):
		print str(locNum + 1) + ': ' + locs[fusRoDah].getName()
		fusRoDah = fusRoDah + 1
		#print nowLocName
		#print nowLocGo
		locNum = locNum + 1
		#print locNum
	#print 'You made it!'
	wheretoGo = getNum()
	#wordsOrNum = nowLocGo[int(wheretoGo) - 1]
	#print wordsOrNum
	while True:
		try:
			return nowLocGo[int(wheretoGo) - 1]
		except IndexError:
			print 'Whoops! Try again with a proper number this time!'
			wheretoGo = getNum()
		except ValueError:
			print 'Whoops! Try again with a real number this time!, not just a letter or a word!'
			wheretoGo = getNum()		

def swapLocation(nowLocation, soonLocation):
	bypass = nowLocation
	#nowLoc = bypass
	nowLocGo = locs[bypass].whereCanGo
	nowLocType = locs[bypass].getLocType()
	nowLocName = locs[bypass].getName()
	nowLocNum = locs[bypass].getNumLocation()
	#^^ exists in a state of bloody stupid.
	"""return nowLoc
	print 'Hi a'
	if nowLocType == 'Location' or nowLocType == 'containerLocation':
		print 'Hi b'
	print nowLocType
	print 'Hi c'"""
	if nowLocType in ('containerLocation', 'Location'):
		print "Where do you want to go?"
		locNum = 0
		#print 'bobbypin'
		
		#while locNum < len(nowLocGo):
		activeLocation = isBorken(nowLocGo, locNum, nowLocName, nowLocNum)
		#locNum = 2
		#locNum = isBorken(nowLocGo, locNum, nowLocName)
	else:
		if nowLocType == 'MultipuleLocation':
			locs[bypass].moveTo(soonLocation)

		elif nowLocType == 'BlockedLocation':
			print 'Special code!'
			if invi in locs[bypass].whatItemNeeded():
				print 'Go?'
				return soonLocation
			else:
				print 'You cannot move there'
		else:
			return 'You cannot move from here'


if __name__ == '__main__':
	pass
	stuff = 1
	#while stuff < 5:
	swapLocation(5, 8)
		#stuff += 1
	#while True:
	#	print activeLocation


