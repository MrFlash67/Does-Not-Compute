import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def swapLocation(nowLocation, soonLocation):
	bypass = nowLocation
	#nowLoc = bypass
	nowLocGo = locs[bypass].whereCanGo
	nowLocType = locs[bypass].getLocType()
	#^^ exists in a state of bloody stupid.
	"""return nowLoc
	print 'Hi a'
	if nowLocType == 'Location' or nowLocType == 'containerLocation':
		print 'Hi b'
	print nowLocType
	print 'Hi c'"""
	if nowLocType in ('containerLocation', 'Location'):
		return soonLocation
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
	stuff = 0
	while stuff < 5:
		swapLocation(0, 1)
		stuff += 1
	#while True:
	#	print activeLocation


