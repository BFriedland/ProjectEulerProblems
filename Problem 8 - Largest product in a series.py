'''

This program determines which thirteen adjacent digits in the 1000-digit number given below, when considered separately, multiply each other to the greatest value.

"The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"

'''


the_big_number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"


the_biggest_sub_product = 0


for each_digit_index in range(0, len(the_big_number) - 13):


    if each_digit_index % 50 == 0:
    
        print("each_digit_index == %r" % (each_digit_index))
    
    
    the_current_sub_product = 1
    
    
    
    for each_next_number in range(0, 13): # Ah, the joy of spending 15 minutes debugging arithmetic only to discover I forgot how zero indexing works yet again.
    
        the_current_sub_product *= int(the_big_number[(each_digit_index + each_next_number)])
        
        
        
    if the_current_sub_product > the_biggest_sub_product:
        
        the_biggest_sub_product = the_current_sub_product
        
        print("\n  discovered at each_digit_index == %r . . ." % (each_digit_index))

        ## This could probably be constructed more algorithmically, but this way makes the 1000-digit number less lonely.
        print("\nNew highest sub product found:\n     %r * %r * %r * %r * %r * %r * %r * %r * %r * %r * %r * %r * %r\n        == %r\n" % (int(the_big_number[(each_digit_index + 0)]), int(the_big_number[(each_digit_index + 1)]), int(the_big_number[(each_digit_index + 2)]), int(the_big_number[(each_digit_index + 3)]), int(the_big_number[(each_digit_index + 4)]), int(the_big_number[(each_digit_index + 5)]), int(the_big_number[(each_digit_index + 6)]), int(the_big_number[(each_digit_index + 7)]), int(the_big_number[(each_digit_index + 8)]), int(the_big_number[(each_digit_index + 9)]), int(the_big_number[(each_digit_index + 10)]), int(the_big_number[(each_digit_index + 11)]), int(the_big_number[(each_digit_index + 12)]), the_biggest_sub_product))
      

      
print("\n\nthe_biggest_sub_product == %r" % (the_biggest_sub_product))


input("\n\nPress enter to end program . . .\n> ")       
