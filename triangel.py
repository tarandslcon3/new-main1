def twoloops(n):
    if n<=0:
        return None
    for i in range (1, n+1):
        space = "" * (n-1)
        stars = "*" * (2*i -1)
        print(space + stars + space)
        # print (i * "*", 'outloop' )
        # for j in range (1, n+1):


print (twoloops(5))
