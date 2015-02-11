import DoesNotComputeCode
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth():
	if locs[activeLocation].whereCanGo[0] == -1:
		print 'You cannot go this way.'
	else:
		return locs[activeLocation].whereCanGo[0]
def goSouth():
	if locs[activeLocation].whereCanGo[2] == -1:
		print 'You cannot go this way.'
	else:
		return locs[activeLocation].whereCanGo[2]
def goEast():
	if locs[activeLocation].whereCanGo[1] == -1:
		print 'You cannot go this way.'
	else:
		return locs[activeLocation].whereCanGo[1]
def goWest():
	#Where the skys are blue....
	if locs[activeLocation].whereCanGo[3] == -1:
		print 'You cannot go this way.'
	else:
		return locs[activeLocation].whereCanGo[3]
if __name__ == "__main__":
	print "Kay"