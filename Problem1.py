'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000

'''


import numpy as np


def main():
    sum = 0
    for i in range(1000):
        if(np.mod(i,3)==0 or np.mod(i,5)==0):
            sum = sum + i
    print(sum)

if __name__=="__main__":
    main()