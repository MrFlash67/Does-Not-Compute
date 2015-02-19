import DoesNotComputeCode, DoesNotComputeFunctions
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth(nowLoc):
	if locs[nowLoc].whereCanGo[0] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return locs[nowLoc].whereCanGo[0]

def goEast(nowLoc):
	if locs[nowLoc].whereCanGo[1] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return locs[nowLoc].whereCanGo[1]

def goSouth(nowLoc):
	if locs[nowLoc].whereCanGo[2] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return locs[nowLoc].whereCanGo[2]

def goWest(nowLoc):
	#Where the skys are blue....
	if locs[nowLoc].whereCanGo[3] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
			return locs[nowLoc].whereCanGo[3]
