from DoesNotComputeClasses import *

everything = [MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', 
['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.',
'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.'),
Location(1, 'You are in a computer, north of where you were. There is a wall of fire just in front of you.', (0, 3, 2), "Wall Of Fire", "Has a wall of fire. Needs an item to pass. TBI."),
containerLocation(['TELNET FIRE EXTINGLISHER', 'APPLE PLOT TOKEN'], 2, 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN. Better take both.', (1,), 'Supply Room', 'Has stuff in it.'),
Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom'),
]

if __name__ == '__main__':
	print "Name is main!"
	print everything[0].getDesc()
	print everything[1].getDesc()
	print everything[2].getDesc()
	print everything[3].getDesc()