import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def isBorken(nowLocGo, locNum ,nowLocName):
	while locNum < len(nowLocGo):
		print 'Hi! ' + str(locNum)
		#print locNum
		print len(nowLocGo)
		locNum += 1
		print nowLocName
		print "Hi! " + str(locNum)
		return locNum
	print 'You made it!'
def swapLocation(nowLocation, soonLocation):
	bypass = nowLocation
	#nowLoc = bypass
	nowLocGo = locs[bypass].whereCanGo
	nowLocType = locs[bypass].getLocType()
	nowLocName = locs[bypass].getName()
	#^^ exists in a state of bloody stupid.
	"""return nowLoc
	print 'Hi a'
	if nowLocType == 'Location' or nowLocType == 'containerLocation':
		print 'Hi b'
	print nowLocType
	print 'Hi c'"""
	if nowLocType in ('containerLocation', 'Location'):
		print "Where do you want to go?"
		locNum = 1
		print 'bobbypin'
		
		while locNum < len(nowLocGo):
			locNum = isBorken(nowLocGo, locNum, nowLocName)
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


