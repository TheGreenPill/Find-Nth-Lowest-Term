def getNthLowest(nums, level):
    # Levellist (type: list) will be used to arrange all numbers (integers/ floats) in ascending order. It will not have any repeated elements.
    # x (type: integer) will be used in a while loop later on in the code to cycle through a list.
    levellist, x = [""], 0
    
    # The initial list is arranged in ascending order using the .sort() inbuilt function in Python.
    nums.sort()
    
    # This while loop cycles through the list nums indirectly. The reason for not using a for loop here is because using the while loop, we can skip ahead in the loop so as to add all unique elements of nums to levellist.
    while x < len(nums):
        
        #Checks if the current element occurs more than once, if so then skip some indices to go to the next unique element.
        if nums.count(nums[x]) > 1:
            x += nums.count(nums[x]) - 1
            
        # Add element on index x to the list levellist
        levellist.append(nums[x])
        
        # Increment index by one.
        x += 1
        
    # check which level is being asked for, and repond accordingly.
    if level >= len(levellist) or level < 0:
        
        # Return standard response for any numbers less than one, or greater than number of unique numbers.
        return("")
    else:
        
        # Return Nth lowest number is level (N) is valid.
        return(levellist[level])
        
# Uncomment the next line and run the program for a trial.
# print(getNthLowest([8, 4, 5, 8, 6, 1, 2, 3], 7))