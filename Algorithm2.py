# Richard Perez
# Algorithm 2
# R.perez4@csu.fullerton.edu

def minSwaps(row):
    # initzializing variables 
    swapped = 0
    seat = {}  
    
    for i, person in enumerate(row):  
        # save count of seats 
        seat[person] = i
    
    for i in range(0, len(row), 2):  
        # get the first person in the row
        first_person = row[i]
        
        # get the correct partner
        second_person = first_person ^ 1  
        
        if row[i + 1] != second_person:
            # if the second person is not next to the first person we swap
            swapped += 1

            # swaped here
            second_person_index = seat[second_person]
            
            # swap the second person with the adjacent to the first person 
            row[i + 1], row[second_person_index] = row[second_person_index], row[i + 1]
            
            # update the dictionary's seating
            seat[row[second_person_index]] = second_person_index
            seat[row[i + 1]] = i + 1
    
    return swapped

def main():
    # our sample cases 
    first_row = [0, 2, 1, 3]
    second_row = [3, 2, 0, 1]
    
    # calling the function for both sample cases
    print(minSwaps(first_row))
    print(minSwaps(second_row))
    print("All couples seated side by side already")
    
    # prompt the user for different numbers
    response = input("Do you want to test different numbers? (y/n): ")
    if response.lower() == 'y':
        num_people = int(input("Enter the number of people in the row (keep it even): "))
        print("Enter the seat numbers of the people in the row: ")
        
        # call the function and print the results 
        row = list(map(int, input().split()))
        print("Minimum number of swaps required to seat all couples together:", minSwaps(row))

if __name__ == "__main__":
    main()
