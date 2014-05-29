'''

This program finds the first (and only) Pythagorean triplet for which a + b + c = 1000, and also prints the product of a*b*c.

"A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."

ref: < https://projecteuler.net/problem=9 >

'''

import math

maximum_value = 1000

a = 1
b = 2
c = 0

answer_found = False

while answer_found == False:

    while (a < (maximum_value / 2)) and answer_found == False:
    
        while (b < (maximum_value / 2)) and answer_found == False:
        
            if ((c - int(c)) == 0):
        
                if (a + b + c == maximum_value):
        
                    print("\nMatch found.\n  %d + %d == %d\n  %d + %d + %d == %d" % (a**2, b**2, c**2, a, b, c, maximum_value))
                    print("    Project Euler: a*b*c = %r" % int((a * b * c)))
                    
                    answer_found = True
            
                else:
            
                    print("\nFound a non-match.\n  %d + %d == %d\n  %d + %d + %d == %d" % (a**2, b**2, c**2, a, b, c, (a + b + c)))
        
                    ## prepare for the next pass here
                    b += 1
                
                    c = ((a ** 2) + (b ** 2))
                    c = math.sqrt(c)
        
            else:
            
                ## prepare for the next pass here too
                b += 1
                
                c = ((a ** 2) + (b ** 2))
                c = math.sqrt(c)
        
        a += 1    
        
        ## reinitialize b to the lowest number that fits the naive criteria
        b = (a + 1)


input("\n\nPress enter to end program . . .\n> ")
