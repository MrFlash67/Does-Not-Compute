import DoesNotComputeCode, DoesNotComputeFunctions
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth(nowLoc):
	if locs[nowLoc].whereCanGo[0] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		if locs[nowLoc].getLocType == 'BlockedLocation' and not locs[nowLoc].getIsOpen():
			return locs[nowLoc].whereCanGo[0]
		else:
			return locs[nowLoc].whereCanGoUnlocked[0]
		

def goEast(nowLoc):
	if locs[nowLoc].whereCanGo[1] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		if locs[nowLoc].getLocType == 'BlockedLocation' and not locs[nowLoc].getIsOpen():
			return locs[nowLoc].whereCanGo[1]
		else:
			return locs[nowLoc].whereCanGoUnlocked[1]

def goSouth(nowLoc):
	if locs[nowLoc].whereCanGo[2] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		if locs[nowLoc].getLocType == 'BlockedLocation' and not locs[nowLoc].getIsOpen():
			return locs[nowLoc].whereCanGo[2]
		else:
			return locs[nowLoc].whereCanGoUnlocked[2]

def goWest(nowLoc):
	#Where the skys are blue....
	if locs[nowLoc].whereCanGo[3] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		if locs[nowLoc].getLocType == 'BlockedLocation' and not locs[nowLoc].getIsOpen():
			return locs[nowLoc].whereCanGo[3]
		else:
			return locs[nowLoc].whereCanGoUnlocked[3]