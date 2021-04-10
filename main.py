#Combinations and Permutations Calculator

import math
import os
import random
import re
import sys
import string

if __name__ == '__main__':
    print("How many different numbers are possible? (n)")
    n = int(input())
    print("How many numbers are used? (r)")
    r = int(input())
    order = input("Is the order of the numbers important? (yes or no)")
    repeat = input("Can you repeat a number? (yes or no)")
    
    if(order == "yes" and repeat == "yes"):
        print("Permutations: ")
        print(abs(n)**abs(r))
    
    elif(order == "yes" and repeat == "no"):
        if(r > n):
            print("Error: Cannot detect number of permutations since r > n")
        elif(r <= 0):
            print("Error: Cannot detect number of permutations since r is less than or equal to 0")
        else:
            nfactorial = 1
            nrfactorial = 1
            for i in range(1, n + 1):
                nfactorial = nfactorial*i
            
            for j in range(1, n-r + 1):
                nrfactorial = nrfactorial*j
            
            print("Permutations: ")
            print(nfactorial / nrfactorial)
            
    
    elif(order == "no" and repeat == "yes"):
        if(n <= 0):
            print("Error: Cannot detect number of combinations since n is less than or equal to 0")
            
        elif(r == 0):
            print("Error: Cannot detect number of combinations since r is 0")
            
        elif(r < 0):
            print("Combinations: ")
            print("1")
        
        else:
            rnfactorial = 1
            rfactorial = 1
            nfactorial = 1
            
            for i in range(1, r + n):
                rnfactorial = rnfactorial*i
                
            for j in range(1, r + 1):
                rfactorial = rfactorial*j
                
            for k in range(1, n):
                nfactorial = nfactorial*k
        
            print("Combinations: ")
            print(rnfactorial / (rfactorial * nfactorial))
        
    elif(order == "no" and repeat == "no"):
        if(n == 0):
            print("Error: Cannot detect number of combinations since n is less than or equal to 0")
            
        elif(r == 0):
            print("Error: Cannot detect number of combinations since r is 0")
            
        elif(r < 0):
            print("Combinations: ")
            print("1")
        
        elif(r > n):
            print("Error: Cannot detect number of permutations since r > n")
        
        else:
            nfactorial = 1
            rfactorial = 1
            nrfactorial = 1
            
            for i in range(1, n+1):
                nfactorial = nfactorial*i
                
            for j in range(1, r + 1):
                rfactorial = rfactorial*j
                
            for k in range(1, n - r + 1):
                nrfactorial = nrfactorial*k
        
            print("Combinations: ")
            print(nfactorial / (rfactorial * nrfactorial))        
    else:
        print("Error: Cannot detect number of permutations")
    
