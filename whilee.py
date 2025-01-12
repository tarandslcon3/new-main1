def even_while():
    n =0
    # if n<=0:
    #     return None
    while n <= 21:
        if n %2 ==0:
            print (n,"even")
        else:
            print (n, "odd")
        n+=1

print (even_while())