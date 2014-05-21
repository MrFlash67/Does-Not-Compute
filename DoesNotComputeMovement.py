import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def swapLocation(nowLocation, soonLocation):
	nowLoc = locs[nowLocation].whereCanGo()
	return nowLoc



if __name__ == '__main__':
	pass
	word = swapLocation(0, 1)
	print '%s' % (word,)
	#while True:
	#	print activeLocation
