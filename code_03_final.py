def deep_rvrs(tup):                                                                         # define a function that reverses a tuple
    return tuple(map(lambda x: deep_rvrs(x) if isinstance(x, tuple) else x, tup[::-1]))     # Recursively reverses the tuple

def get_tuple_input():                                                                      # define a function that prompts for a tuple input
    from ast import literal_eval                                                            # import the literal_eval function from the ast module
    input_str = input("Type the input '(1,2,3,4)/(1,(2,3),4)': ")                           # prompt for input
    try:
        result = literal_eval(input_str)                                                    # try to evaluate the input as a tuple
        if isinstance(result, tuple):                                                       # if the input is a tuple, return the tuple
            return result                                                                   # return the tuple
        else:
            print("Invalid input! input must be a tuple.")                                  # otherwise, print an error message
            return get_tuple_input()                                                        # Recursively prompt for correct input
    except:
        print("Invalid input! enter a valid tuple.")                                        # otherwise, print an error message
        return get_tuple_input()                                                            # Recursively prompt for correct input

if __name__ == "__main__":                                                                  # if the file is run directly
    print("Please input the first tuple:")
    a = get_tuple_input()                                                                   # prompt for input
    reversed_a = deep_rvrs(a)                                                               # reverse the tuple
    print(f"Input: {a}")                                                                    # print the input
    print(f"Output: {reversed_a}\n")                                                        # print the output

    print("Please input the second tuple:")
    tpl = get_tuple_input()                                                                 # prompt for input
    reversed_tpl = deep_rvrs(tpl)                                                           # reverse the tuple
    print(f"Input: {tpl}")                                                                  # print the input
    print(f"Output: {reversed_tpl}")                                                        # print the output
