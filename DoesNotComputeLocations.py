from DoesNotComputeClasses import *

locs = [
Location(0, 'You are in a computer. A banana runs at you, then promptly fades away.', [1,-1,-1,2], 'Starting room', 'Requires  5 uses of the \'go\' command'),
BlockedLocation(1, 'You are in a computer, north of where you were. There is a wall of fire just in front of you.', [-1, -1, 0, 2], "Wall Of Fire", "Has a wall of fire. Needs an item to pass. TBI.", [3,-1,0,2], 'TELNET FIRE EXTINGLISHER'),
containerLocation(['TELNET FIRE EXTINGLISHER', 'APPLE PLOT TOKEN'], 2, 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN. Better take both.', [-1, 1, 0, -1], 'Supply Room', 'Has stuff in it.', 'You are in a supply room. You see where a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN would be, if they were stil there.'),
containerLocation(['USELESS MAGIC WAND'], 3, 'There is a small spike pit and a magic wand. Don\'t take the wand.', [4,-1,1,-1], 'Pre-Boss room', 'Requires APT to get in, has entry to bossRoom', 'There is a small spike pit and a lack of a magic wand.'),
BossLocation(4, 'You are in an arena.', [1,2,3,4], 'Arena', 'Has a boss.', 'King Banana With Gun'),
]

if __name__ == '__main__':
	print "Name is main!"
	print locs[0].getDesc()
	print locs[1].getDesc()
	print locs[2].getDesc()
	print locs[3].getDesc()
	print locs[4].getDesc()