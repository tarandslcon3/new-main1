def twoloops(n, x, c):

    for i in range(n):
        for j in range (x):
            # print (i, j, end=" \t")
            for k in range(c):
                print (i+1,j+1,k+1,end=" \t")
            print()
        print()

print (twoloops(1,2,1))
