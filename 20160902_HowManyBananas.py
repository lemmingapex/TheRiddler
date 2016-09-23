import math

# inputs
initalNumberOfBananas = 3000
numberOfUnitsToDestination = 1000
cammelCompacity = 1000
bananasPerUnitThatCammelConsumes = 1


distanceToTravel = numberOfUnitsToDestination
numberOfBananasRemainingAtDistanceToTravel = initalNumberOfBananas
while(distanceToTravel > 0):
	#print("distanceToTravel", distanceToTravel)
	#print("numberOfBananasRemainingAtDistanceToTravel", numberOfBananasRemainingAtDistanceToTravel)
	decreaseInBananas = math.ceil(numberOfBananasRemainingAtDistanceToTravel/cammelCompacity) * bananasPerUnitThatCammelConsumes
	#print("decreaseInBananas", decreaseInBananas)
	numberOfBananasRemainingAtDistanceToTravel = numberOfBananasRemainingAtDistanceToTravel - decreaseInBananas
	distanceToTravel = distanceToTravel - 1

print("numberOfBananasRemainingAtZeroDistanceToTravel", numberOfBananasRemainingAtDistanceToTravel)
