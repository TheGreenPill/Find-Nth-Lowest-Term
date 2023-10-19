# By default this function will find the Nth lowest number passed through it. If the line "nums.sort()" is changed to "nums.sort(reverse="True") this will change, and then the function will find the Nth greatest number.

def getNthGreatestOrLowest(nums, level):
    # Levellist (type: list) will be used to arrange all numbers (integers/ floats) in ascending order. It will not have any repeated elements.
    # x (type: integer) will be used in a while loop later on in the code to cycle through a list.
    levellist = [""]
    
    # The initial list is arranged in ascending order using the .sort() inbuilt function in Python.
    nums.sort()
    
    # Remove duplicates by simply converting list to set and back to list again, and then append nums to levellist.
    levellist.extend(list(set(nums)))
    
    # check which level is being asked for, and repond accordingly.
    if level >= len(levellist) or level < 0:
        
        # Return standard response for any numbers less than one, or greater than number of unique numbers.
        return("")
    else:
        
        # Return Nth lowest number is level (N) is valid.
        return(levellist[level])
        
# Uncomment the next line and run the program for a trial.
# print(getNthLowest([8, 4, 5, 8, 6, 1, 2, 3], 7))
