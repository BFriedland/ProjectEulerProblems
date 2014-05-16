"""

This program finds the largest prime factor of a given number.

Note: is_prime() was my head-on approach to finding primes, based on the definitions I had been given for primeness.
It turns out there are much more efficient ways to find prime numbers rapidly, one of which I will include in a comment at the bottom as the function: find_greatest_prime_factor()
Credit for that solution: Javi's C# solution transcribed to Python by BF < ref: https://projecteuler.net/thread=3;page=8 at 29 Apr 2014 05:20 pm  >

"The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"

"""



import math


def is_prime(x):

    ''' Return True if the argument is prime and False if it is not. '''

    ## Non-integer numbers cannot be primes.
    if ((x % int(x)) != 0):
        
        return False
    
    
    ## Check for evenness. Wipes out half of all possible checks if no such check was used.
    
    
    if (x % 2 != 0):
        ## Implicitly check for clean divisibility by 3, too.
        x_handler = ( (x // 3) + 1 ) #the +1 is because -1 is necessary for checking, see below
    
    ## otherwise it's even, and therefore not prime.
    else:
    
        return False

    if (x < 2):
    
        return False
        
    elif (x == 2):
    
        return True
        
    else:
    
        while (x_handler > 2):
        
            if ((x % (x_handler - 1)) == 0):
            
                return False    
                
            x_handler = (x_handler - 1)
            

        return True            
        
        
def generate_ascending_primes_up_to_this_number(limiting_number):
    
    
    number_to_be_checked = 2 # the first prime
    
    while number_to_be_checked <= int(limiting_number):
        
        if is_prime(number_to_be_checked):
            
            yield number_to_be_checked
            
        number_to_be_checked += 1


        

def find_greatest_prime_factor(the_suspect):

    ## Using math.sqrt() because that's when the quotient passes the divisor.
    for each_prime in generate_ascending_primes_up_to_this_number(math.sqrt(the_suspect)):#the_suspect):

        
        ## Update the state so the while loop can terminate.

        the_quotient = the_suspect / each_prime
        
        if each_prime <= the_quotient:    
           
            if ((the_quotient % 1) == 0):
                

                print("    Clean division found. %r / %r == %r" % (the_suspect, each_prime, the_quotient))

                
                if is_prime(the_quotient):
                    
                    print("      Match found. %r / %r == %r" % (the_suspect, each_prime, the_quotient))
                
                    break

                
        ## If the quotient is lower than the divisor, it must be PAST the upper limit, since quotients below the highest prime checked so far cannot be a higher prime than the highest checked, as quotients will only keep going down.
        else:
        
            break
            
            

    
    
find_greatest_prime_factor(600851475143)    
    
while True:

    try:
        user_input_goes_here = int(input("\nWhat number to find the greatest prime factor of?\n> "))
        find_greatest_prime_factor(user_input_goes_here)  
        
    except ValueError:
        print("\nPlease enter a positive integer.\n")
        
kek = input("\n\nPress enter to end program . . .\n> ")


"""

## Javi's C# solution transcribed to Python < ref: https://projecteuler.net/thread=3;page=8 at 29 Apr 2014 05:20 pm  >

#number = 600851475143


def find_greatest_prime_factor(number):
    
    ''' Return the greatest prime factor of a number. '''
            
    ## This algorithm works because you can rely on the fact that the result of dividing a number by one of its factors will, itself, be a multiple of the original number's greatest prime factor. The algorithm stops when the dividend and divisor flip.
    
    ## Also, the GPF of 4 is 2 which this algorithm would otherwise not catch... but that's not a super important thing to know...
    if (number == 1):
        print("\nGreatest prime factor == %r" % (1))
        return 1
    elif (number == 2) or (number == 4):
        print("\nGreatest prime factor == %r" % (2))
        return 2        

    
    i = 3 # the factor handler
    
    
    last_checked_number = 0 # used to report the end result
    
    ## The algorithm reduces the size of the number we're checking every time it finds a factor of the number we're checking. It can stop when the dividend and divisor swing around each other. (( which is not actually the sqrt, is it? this algorithm is technically more direct than even needing to use the sqrt at all as a limiting value... ))
    while i <= number:
        
        ## If a number divides by another number evenly, the other number must be a factor of the first number.
        if number % i == 0:

            print("%r mod %r == 0" % (number, i))
            print("    ---> %r == %r / %r" % ((number / i), number, i))
            

            ## This section is 
            if number != 1:
                last_checked_number = i
                
            else:
                last_checked_number = number
            
            ## Next, the critical leap.
            ## The result of dividing a number by its factor will be another number that either is the greatest prime factor of the first number, or is a multiple of the greatest prime factor of the first number.
            ## The logic behind this algorithm is recursion-flavored, but it is not implemented in a recursive structure. It's merely taking advantage of simple properties of factors.
            number = number / i
        
        ## If no clean division was found this pass, increment by 2 (not 1, since we can safely skip all even numbers).
        i += 2

    print("\nGreatest prime factor == %r" % (last_checked_number))   
    return last_checked_number
    
"""    
