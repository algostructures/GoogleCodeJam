'''
Question : Counting Sheep 
Link : https://code.google.com/codejam/contest/6254486/dashboard
'''
#-------------------------------------------------------------------------------
# Name:        Google Code Jam Qualification Round Problem 1
# Link:		   https://code.google.com/codejam/contest/6254486/dashboard
#
# Author:      Saurabh
#
# Created:     09/04/2016
# Copyright:   (c) Saurabh 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def check(s):
    d = (['1','2','3','4','5','6','7','8','9','0'])
    if set(d) == set(s):
        return True
    else:
        return False

def main():
    test = input()
    while test > 0:
        test -= 1
        n = input()
        if n == 0:
            print "INSOMNIA"
        else:
            d = set()
            i = 1
            while(True):
                d.update(list(str(i*n)))
                if(check(d)):
                    print i*n
                    break
                i += 1
if __name__ == '__main__':
    main()

