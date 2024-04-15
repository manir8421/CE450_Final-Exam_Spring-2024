class Fibonacci:                                                # define a class Fibonacci with two attributes val and pre
    def __init__(self, val=0, pre=1):                           # define the constructor of the class Fibonacci
        self.val = val                                          # define the attributes val 
        self.pre = pre                                          # define the attributes pre 

    def nxt(self):                                              # define a method nxt to return the next Fibonacci number
        new_fib = Fibonacci(self.pre, self.val + self.pre)      # define a new Fibonacci object with the value of the previous Fibonacci object plus the previous Fibonacci object
        return new_fib                                          # return the new Fibonacci object 

    def __repr__(self):                                         # define a method __repr__ to return the value of the Fibonacci object 
        return str(self.val)                                    # return the value of the Fibonacci object

if __name__ == "__main__":
    a = Fibonacci()                                             # define a Fibonacci object a 
    print(a)                                                    # print the value of the Fibonacci object a 
    print(a.nxt())                                              
    print(a.nxt().nxt())                                        
    print(a.nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt().nxt())
    print(a.nxt().nxt().nxt().nxt().nxt().nxt())
