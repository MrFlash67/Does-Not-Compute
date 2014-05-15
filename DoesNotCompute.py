import DoesNotComputeCode as dnc, DoesNotComputeFunctions, sys
try:
	print
	'''Commented out for time'''
	#DoesNotComputeFunctions.intro()
	inv = ['no tea']
	loopCount = dnc.gameloop(inv, 0)
except KeyboardInterrupt:
	DoesNotComputeFunctions.exit()