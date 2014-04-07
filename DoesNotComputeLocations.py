from DoesNotComputeClasses import *
everything = [Location(3, 'There is a small spike pit and a magic wand. May as well take the wand.', (1, 4), 'Pre-Boss room', 'Contains WND, requires APT to get in, has entry to bossRoom'),
MultipuleLocation(3, 0, 'You are in a computer. A banana runs at you', (1, ), 'Starting room', 'Requieres  5 uses of the \'go\' command', 
['You cannot move there', 'Are you sure? It looks dangorous.', 'It\'s dangorous to go alone! Don\'t go!', 'It looks just the same, and too much moving to an identical place is bad for you!', 'Fine, go.',
'ERROR: SPPECH OVERFLOW 1', 'ERROR: SPPECH OVERFLOW 2', 'ERROR: SPPECH OVERFLOW 3'], 'Fine, go.'),
containerLocation(['lol', 'wut'], 11, 'A place with items', (900, 67, 42, 1), 'Song of Time', 'I say lol, it contains items, derp')
]

if __name__ == '__main__':
	print "Name is main!"
	print everything[0].getDesc()
	print everything[1].getDesc()
	print everything[2].getDesc()