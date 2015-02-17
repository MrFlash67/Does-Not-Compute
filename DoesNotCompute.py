import DoesNotComputeCode as dnc, DoesNotComputeFunctions, sys, DoesNotComputeMovement
try:
	#DoesNotComputeFunctions.intro()
	inv = ['no tea']
	loopCount = dnc.gameloop(inv, 0)
except KeyboardInterrupt:
	DoesNotComputeFunctions.exit()
