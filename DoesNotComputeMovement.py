import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def swapLocation(nowLocation, soonLocation):
	nowLoc = nowLocation
	nowLocGo = locs[nowLoc].whereCanGo
	nowLocType = locs[nowloc].getLocType
	#^^ exists in a state of bloody stupid.
	#return nowLoc
	if nowLocType == 'Location' or nowLocType == 'ContainerLocation':
		print 'Hi'


if __name__ == '__main__':
	pass
	swapLocation(1, 2)
	#while True:
	#	print activeLocation


