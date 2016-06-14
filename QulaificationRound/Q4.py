#-------------------------------------------------------------------------------
# Name:        Google CodeJam Qualification Round Problem 4
# Link:			https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#
# Author:      Saurabh
#
# Created:     09/04/2016
# Copyright:   (c) Saurabh 2016
# Licence:     <your licence>
#
# Note:		Partial Solution
#-------------------------------------------------------------------------------

def main():
    fo = open("D-small-attempt0.in","r")
    fp = open("output.txt", "w")
    test = int(fo.readline())
    tri = 1
    while test > 0:
        test -= 1
        line = map(int, fo.readline().split())
        k = line[0]
        fp.write("Case #"+str(tri)+": ",)
        for i in range(k):
            fp.write(str(i+1)+" ",)
        fp.write("\n")
        tri+=1



if __name__ == '__main__':
    main()
