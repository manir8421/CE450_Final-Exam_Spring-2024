def verify_add(m, ls):                                              # Defines a function verify_add that takes two parameters: m (a target sum) and ls (a list or range of integers).                                                                                                                                                                                                                                                                       
    seen = set()                                                    # Creates a set called seen.
    for number in ls:                                               # Iterates through the list or range of integers.
        complement = m - number                                     # Calculates the complement of the current number.
        if complement in seen:                                      # If the complement is in the set, then the function returns True.
            return True                                             # Returns True.
        else:                                                       # If the complement is not in the set, then the function adds the current number to the set.
            seen.add(number)                                        # Adds the current number to the set.
    return False                                                    # Returns False.

def get_target_sum():                                               # Defines a function get_target_sum that takes no parameters.
    while True:                                                     # Loops until a valid input is entered.
        try:                                                        
            return int(input("Enter the target sum (m): "))         # Returns the target sum (m).
        except ValueError:                                          # If the input is not an integer, then the function prints an error message and loops again.
            print("Invalid input. Please enter an integer.")        # Prints an error message.

def get_number_list():                                              # Defines a function get_number_list that takes no parameters.
    while True:                                                     # Loops until a valid input is entered.
        input_str = input("Enter the list of numbers '[1,2,3]/range(0,10,2)': ").replace(' ', '')   # Prompts the user to enter a list or range of integers.
        try:    
            numbers = eval(input_str)                               # Evaluates the input string and assigns it to the variable numbers.
            if isinstance(numbers, list) or isinstance(numbers, range):   # If the input is a list or range, then the function returns the list or range.
                return numbers                                      # Returns the list or range.
            else:                                                   # If the input is not a list or range, then the function prints an error message and loops again.
                print("Invalid input. Please enter list/range.")            
        except:                                                         
            print("Invalid input. Please ensure list/range.")           

if __name__ == "__main__":
    m = get_target_sum()                                                    # Prompts the user to enter the target sum (m).
    ls = get_number_list()                                                  # Prompts the user to enter a list or range of integers.
    
    if isinstance(ls, range):                                               # If the input is a range, then the function prints the range.
        print(f"verify_add ({m}, range({ls.start}, {ls.stop}, {ls.step}))")  # Prints the range.
    else:
        formatted_list = str(ls).replace(' ', '')                          # If the input is a list, then the function prints the list.
        print(f"verify_add ({m}, {formatted_list})")                       # Prints the list.
    
    result = verify_add(m, ls)                                              # Calls the function verify_add and assigns the result to the variable result.
    print(result)                                                           # Prints the result.
