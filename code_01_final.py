from functools import wraps                                             # for the @wraps decorator

def trc1(f):                                                            # decorator function
    @wraps(f)                                                           # preserve the name and docstring of the function
    def wrapped(*args, **kwargs):                                       # wrapper function
        arg_str = ', '.join(repr(arg) for arg in args)                  # convert the arguments to a string
        print(f"Calling <function {f.__name__} at {hex(id(f))}> on argument {arg_str}")  # print the function name and arguments
        result = f(*args, **kwargs)                                     # Execute the function and store the result
        return result                                                   # return the result
    return wrapped                                                      # return the wrapper function

@trc1                                                                   # decorator
def sqr(x):                                                             # function to be decorated
    return x * x                                                        # return the result

@trc1                                                                   # decorator
def sum_sqr(n):                                                         # function to be decorated
    def helper(current):                                                # helper function
        if current > n:                                                 # base case
            return 0                                                    # return 0
        else:                                                           # recursive case
            result = sqr(current)                                       # call sqr on current
            return result + helper(current + 1)                         # return the result and call helper on current + 1
    return helper(1)                                                    # call helper on 1

def get_integer_input(prompt="Enter a positive integer: "):             # function to get an integer from the user
    while True:                                                         # loop until a valid input is given
        try:                                                            # try to get an integer from the user
            value = int(input(prompt))                                  # get the integer from the user
            if value <= 0:                                              # check if the integer is positive
                raise ValueError("Please enter a positive integer.")    # raise a ValueError if the integer is not positive
            return value                                                # return the integer
        except ValueError as e:                                         # if a ValueError is raised
            print(f"Invalid input. {e}")                                # print the error message

if __name__ == "__main__":
    x = get_integer_input("Type an integer value: ")                    # get an integer from the user
    print(sqr(x))                                                       # call to sqr, will print trace and result
    print(sum_sqr(x))                                                   # call to sum_sqr, will print trace and results recursively
