from DoesNotComputeClasses import *

locs = [
Location(0, 'You are in a computer. A banana runs at you', [1,-1,-1,2], 'Starting room', 'Requires  5 uses of the \'go\' command'),
BlockedLocation(1, 'You are in a computer, north of where you were. There is a wall of fire just in front of you.', [3, -1, 0, 2], "Wall Of Fire", "Has a wall of fire. Needs an item to pass. TBI.", [3,0,2], 'TFE'),
containerLocation(['TELNET FIRE EXTINGLISHER', 'APPLE PLOT TOKEN'], 2, 'You are in a supply room. You see a TELNET FIRE EXTINGLISHER and an APPLE PLOT TOKEN. Better take both.', [-1, 1, 0, -1], 'Supply Room', 'Has stuff in it.'),
Location(3, 'There is a small spike pit and a magic wand. Don\'t take the wand.', [4,-1,-1,1], 'Pre-Boss room', 'Requires APT to get in, has entry to bossRoom'),
BossLocation(4, 'You are in an arena.', [5,-1,-1,-1], 'Arena', 'Has a boss.', 'King Banana With Gun', 0),

]

if __name__ == '__main__':
	#print "Name is main!"
	#print locs[0].getDesc()
	#print locs[1].getDesc()
	#print locs[2].getDesc()
	#print locs[3].getDesc()
	#print locs[4].getDesc()
	#print locs[4].attack(0)
	#print locs[4].attack(1)
	#print locs[4].attack(2)
	stuff = 0
	while stuff < 5:
		locs[0].moveTo(1)
		stuff += 1