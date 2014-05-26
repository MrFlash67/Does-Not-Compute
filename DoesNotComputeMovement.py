import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def swapLocation(nowLocation, soonLocation):
	bypass = nowLocation
	#nowLoc = bypass
	nowLocGo = locs[bypass].whereCanGo
	nowLocType = locs[bypass].getLocType()
	#^^ exists in a state of bloody stupid.
	'''return nowLoc
	print 'Hi a'
	if nowLocType == 'Location' or nowLocType == 'containerLocation':
		print 'Hi b'
	print nowLocType
	print 'Hi c' '''


if __name__ == '__main__':
	pass
	swapLocation(3, 3)
	#while True:
	#	print activeLocation


