import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth():
	return locs[activeLocation].whereCanGo[0]
def goSouth():
	return locs[activeLocation].whereCanGo[2]
def goEast():
	return locs[activeLocation].whereCanGo[1]
def goWest():
	#Where the skys are blue....
	return locs[activeLocation].whereCanGo[3]
if __name__ == "__main__":
	print "Kay"