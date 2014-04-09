from DoesNotComputeClasses import *

locs = [MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', 
['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.',
'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.'),
BlockedLocation(1, 'You are in a computer, north of where you were. There is a wall of fire just in front of you.', (0, 3, 2), "Wall Of Fire", "Has a wall of fire. Needs an item to pass. TBI."),
containerLocation(['TELNET FIRE EXTINGLISHER', 'APPLE PLOT TOKEN'], 2, 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN. Better take both.', (1,), 'Supply Room', 'Has stuff in it.'),
Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom'),
#Needs to be Boss Location vv
Location(4, 'There is a great, big, menancing banana next to you.', (5, 6), 'Arena', 'Has a boss.')
]

if __name__ == '__main__':
	print "Name is main!"
	print locs[0].getDesc()
	print locs[1].getDesc()
	print locs[2].getDesc()
	print locs[3].getDesc()
	print locs[4].getDesc()