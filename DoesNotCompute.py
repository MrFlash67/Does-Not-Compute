import DoesNotComputeCode as dnc, DoesNotComputeFunctions, sys, DoesNotComputeMovement_old
try:
	#print DoesNotComputeMovement_old.activeLocation
	#DoesNotComputeMovement_old.activeLocation = 0
	#print DoesNotComputeMovement_old.activeLocation
	#import DoesNotComputeMovement_old
	#print DoesNotComputeMovement_old.activeLocation
	print
	'''Commented out for time'''
	#DoesNotComputeFunctions.intro()
	inv = ['no tea']
	loopCount = dnc.gameloop(inv, 0)
except KeyboardInterrupt:
	DoesNotComputeFunctions.exit()
