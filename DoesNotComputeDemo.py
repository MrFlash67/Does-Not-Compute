import DoesNotComputeCode as dnc, DoesNotComputeFunctions, sys, DoesNotComputeMovement
try:
	#print DoesNotComputeMovement.activeLocation
	#DoesNotComputeMovement.activeLocation = 0
	#print DoesNotComputeMovement.activeLocation
	#import DoesNotComputeMovement
	#print DoesNotComputeMovement.activeLocation
	print
	DoesNotComputeFunctions.intro()
	inv = ['no tea']
	loopCount = dnc.gameloop(inv, 0)
except KeyboardInterrupt:
	DoesNotComputeFunctions.exit()
