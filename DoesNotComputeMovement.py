import DoesNotComputeCode, DoesNotComputeFunctions
from DoesNotComputeLocations import locs
activeLocation = 0
def goNorth(nowLoc):
	whereCanGo = locs[nowLoc].whereCanGo
	print whereCanGo
	print whereCanGo[0]
	if locs[nowLoc].getLocType == 'BlockedLocation' and locs[nowLoc].getIsOpen():
		whereCanGoUnlocked = locs[nowLoc].whereCanGoUnlocked()
		return whereCanGoUnlocked[0]
	elif whereCanGo[0] == -1:
			print 'You cannot go this way.'
			return nowLoc
	else:
		return whereCanGo[0]
		

def goEast(nowLoc):
	whereCanGo = locs[nowLoc].whereCanGo
	if locs[nowLoc].getLocType == 'BlockedLocation' and locs[nowLoc].getIsOpen():
		whereCanGoUnlocked = locs[nowLoc].whereCanGoUnlocked()
		return whereCanGoUnlocked[1]
	elif whereCanGo[1] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return whereCanGo[1]


def goSouth(nowLoc):
	whereCanGo = locs[nowLoc].whereCanGo
	if locs[nowLoc].getLocType == 'BlockedLocation' and locs[nowLoc].getIsOpen():
		whereCanGoUnlocked = locs[nowLoc].whereCanGoUnlocked()
		return whereCanGoUnlocked[2]
	elif whereCanGo[2] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return whereCanGo[2]


def goWest(nowLoc):
	#Where the skys are blue...
	whereCanGo = locs[nowLoc].whereCanGo
	if locs[nowLoc].getLocType == 'BlockedLocation' and locs[nowLoc].getIsOpen():
		whereCanGoUnlocked = locs[nowLoc].whereCanGoUnlocked()
		return locs[nowLoc].whereCanGoUnlocked[3]
	elif whereCanGo[3] == -1:
		print 'You cannot go this way.'
		return nowLoc
	else:
		return whereCanGo[3]