from DoesNotComputeClasses import *

locs = [
Location(0, 'You are in a computer. A banana runs at you, then promptly fades into nothingness.', [1, -1, -1, -1], 'Starting room', 'Requires  5 uses of the \'go\' command'),
BlockedLocation(1, 'You are in a computer, north of that incident with the fading banana. There is a wall of fire just in front of you.', [-1, -1, 0, 2], "Wall Of Fire", "Has a wall of fire. Needs an item to pass. TBI.", [3,-1,0,2], 'TELNET FIRE EXTINGLISHER', 'You are in a computer, north of where you were. There is the charred remains of a wall of fire in front of you.'),
containerLocation(['TELNET FIRE EXTINGLISHER', 'APPLE PLOT TOKEN'], 2, 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN. Better take both.', [-1, 1, -1, -1], 'Supply Room', 'Has stuff in it.', 'You are in a supply room. You see where a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN would be, if they were stil there.'),
containerLocation(['USELESS MAGIC WAND'], 3, 'There is a small spike pit and a magic wand. Don\'t take the wand.', [4,-1,1,-1], 'Pre-Boss room', 'Requires APT to get in, has entry to bossRoom', 'There is a small spike pit and a lack of a magic wand.'),
BossLocation(4, 'You are in an arena.', [1,2,3,4], 'Arena', 'Has a boss.', 'King Banana With Gun'),
]

if __name__ == '__main__':
	print "Name is main!"
	for x in locs:
		print x.returnLocationData()
	#print locs[0].returnLocationData()
	#print locs[1].returnLocationData()
	#print locs[2].returnLocationData()
	#print locs[3].returnLocationData()
	#print locs[4].returnLocationData()