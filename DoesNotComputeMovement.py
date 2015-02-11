import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth():
	print locs[activeLocation].whereCanGo[0]
def goSouth():
	print locs[activeLocation].whereCanGo[2]
def goEast():
	print locs[activeLocation].whereCanGo[1]
def goWest():
	#Where the skys are blue....
	print locs[activeLocation].whereCanGo[3]
if __name__ == "__main__":
	print "Kay"