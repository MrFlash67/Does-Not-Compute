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
		moveNow = 1
	else:
		moveNow = 0
	if moveNow == 1:
		return soonLocation
	else:
		if nowLocType == 'MultipuleLocation':
			pass
		elif nowLocType == 'BlockedLocation':
			pass
		else:
		return 'You cannot move from here'


if __name__ == '__main__':
	pass
	
	print swapLocation(1, 3)
	#while True:
	#	print activeLocation


