# Richard Perez
# Algorithm 1
# R.perez4@csu.fullerton.edu

def bestStartingCity(distances, fuel, mpg):
   # initializing variables
	cityCount = len(distances)
	netFuel = 0
	remainingFuel = 0
	bestCity = 0

	# Loop through the cities to find the remaining fuel
	for i in range(cityCount): 
		# this give us our range in mpg
		totalRange = fuel[i] * mpg
		remainingFuel = totalRange - distances[i]
 		
		# Track if trip is even possible
		netFuel += totalRange
		remainingFuel += totalRange
  		
		# if currentFuel below zero then the city is too far
		if (remainingFuel < 0):
			bestCity = i + 1
			remainingFuel  = 0
	# If total fuel is less than 0, return -1	
	return bestCity if netFuel >= 0 else -1


def main():
    # sample input, ans should be 4 
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10

    print("Checking the sample input:", bestStartingCity(distances, fuel, mpg))

    # Prompt the user for different values
    ans = input("Do you want to test different numbers? (y/n): ").strip().lower()

    while ans == 'y':
        # Geting the user inputs for distance, fuel and mpg
        distances = list(map(int, input("Enter the distances between all the cities: ").split()))
        fuel = list(map(int, input("Enter the fuel available at each city: ").split()))
        mpg = int(input("Enter the miles per gallon: "))
		
		# return their best starting city
        print("Preferred starting city:", bestStartingCity(distances, fuel, mpg))
		
		# prompt again!!
        ans = input("Do you want to test different numbers? (y/n): ").strip().lower()


if __name__ == "__main__":
    main()