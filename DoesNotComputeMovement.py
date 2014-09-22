import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def getNum():
	
	wheretoGo = raw_input('Enter in the location number shown above\n< ')
	return wheretoGo
def isBorken(nowLocGo, locNum ,nowLocName, nowLocNum):
	print nowLocGo
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
			print 'You have moved!'
			return nowLocGo[int(wheretoGo) - 1]
		except IndexError:
			print 'Whoops! Try again with a proper number this time!'
			wheretoGo = getNum()
		except ValueError:
			print 'Whoops! Try again with a real number this time!, not just a letter or a word!'
			wheretoGo = getNum()

def swapLocation(nowLocation, invi):
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
	print "Where do you want to go?"
	locNum = 0
	#print 'bobbypin'
	
	#while locNum < len(nowLocGo):
	return isBorken(nowLocGo, locNum, nowLocName, nowLocNum)
	#locNum = 2
	#locNum = isBorken(nowLocGo, locNum, nowLocName)
	locNum = 0
	#print locs[bypass].whatItemNeeded()
	return isBorken(nowLocGo, locNum, nowLocName, nowLocNum)
	

if __name__ == '__main__':
	pass
	stuff = 1
	#while stuff < 5:
	swapLocation(5)
		#stuff += 1
	#while True:
	#	print activeLocation
