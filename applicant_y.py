#python exercise 4 Azvdo

import sys

class straight_line:
    """class straight_line
    represents a straight line
    """

    def __init__(self, a, b, c):
        """constructor
        
        Arguments:
            a {float} -- a in ax + by + c = 0
            b {float} -- b in ax + by + c = 0
            c {float} -- c in ax + by + c = 0
        """
        self.a = a
        self.b = b
        self.c = c

    def integral(self, l_1, l_2):
        """ integral from l_1 to l_2  of y = -a/2b * x - c/b
        
        Arguments:
            l_1 {float} -- represents a vertical line x = l_1
            l_2 {float} -- represents a vertical line x = l_2
        
        Returns:
            float -- area between x = l_1, x = l_2 , ax + by + c = 0 and y = 0
        """
        # area = [-ax^2/2b - cx/b] from l_1 to l_2

        t_1 = (-1 * self.a/(2*self.b)) * pow(l_2, 2) - (self.c/self.b) * (l_2)
        t_2 = (-1 * self.a/(2*self.b)) * pow(l_1, 2) - (self.c/self.b) * (l_1)
        return t_1 - t_2

def main():
    ## error checking for boundaries cases

    # less than 6 args for input
    if (len(sys.argv) != 6):
        print ("please provide only 6 arguments")
        exit("[ERROR] arguments list must have 6 elements")
    
    # all inputs are numbers
    def check_convert_float(x):
        try:
            return float(x) 
        except ValueError:
            print ("provide all arguments as real numbers")
            exit("[ERROR] argument {} not real".format(x))
    
    args = list(map(check_convert_float, sys.argv[1:]))

    # a and b are non-zero
    if args[0] == float(0) or args[1] == float(0):
        print("\"a\" and \"b\" must not be zero")
        exit("[ERROR] a and b must be non-zero")

    # l_1 > l_2
    if args[3] > args[4]:
        print("\"l_1\" must be smaller than \"l_2\"")
        exit("[ERROR]  l_1 > l_2")

    ## program itself
    # line instantiation
    my_line = straight_line(args[0], args[1], args[2])

    # integral calculation
    result = my_line.integral(args[3], args[4])
    print("integral", result)

if __name__ == "__main__":
    main()