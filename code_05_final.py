class Student:                                                                  # define class Student                                                                                                                                         
    def __init__(self, name: str, number_of_courses: int):                      # define constructor with name and number of courses as parameters
        self.name = name                                                        # define name as a parameter of the class
        self.number_of_courses = number_of_courses                              # define number of courses as a parameter of the class

    def __add__(self, other):                                                   # define method __add__ to add two students together
        total_courses = self.number_of_courses + other.number_of_courses        # define total courses as the sum of the number of courses of the two students
        return Student("", total_courses)                                       # return a new student with the total courses as the number of courses of the two students

    def __eq__(self, other):                                                    # define method __eq__ to compare two students based on the number of courses they have taken
        return self.number_of_courses == other.number_of_courses                # return true if the number of courses of the two students are equal and false otherwise 

    def __ne__(self, other):                                                    # define method __ne__ to compare two students based on the number of courses they have taken 
        return not self == other                                                # return true if the number of courses of the two students are not equal and false otherwise

    def __lt__(self, other):                                                    # define method __lt__ to compare two students based on the number of courses they have taken
        return self.number_of_courses < other.number_of_courses                 # return true if the number of courses of the first student is less than the number of courses of the second student and false otherwise
    
    def __gt__(self, other):                                                    # define method __gt__ to compare two students based on the number of courses they have taken
        return self.number_of_courses > other.number_of_courses                 # return true if the number of courses of the first student is greater than the number of courses of the second student and false otherwise

    def __str__(self):                                                          # define method __str__ to return the number of courses of the student as a string 
        return str(self.number_of_courses)                                      # return the number of courses of the student as a string 

    def __repr__(self):                                                         # define method __repr__ to return the number of courses of the student as a string 
        return str(self)                                                        # return the number of courses of the student as a string

# Example data according to questions
a = Student('Peter', 3) 
b = Student('Mike', 4)
c = Student('John', 5)
d = Student('Kelvin', 3)

print(a + b + d)                                                               # print the sum of the number of courses of the two students
print(a != d)                                                                  # print true if the number of courses of the two students are not equal and false otherwise
print(b < c)                                                                   # print true if the number of courses of the first student is less than the number of courses of the second student
