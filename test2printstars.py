def print_stars(n):
    if n <=0:
        print("not going to work")
    for i in range(1, n+1):
        spaces = " " * (n-1)
        stars = "*" * (2 * i - 1)

        print (spaces + stars)

# def print_triangle(n):
#     if n <= 0:
#         print("Input should be a positive integer.")
#         return None
#     for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
#         spaces = " " * (n - i)  # Add spaces to center the stars
#         stars = "*" * (2 * i - 1)  # Odd number of stars for each row
#         print(spaces + stars)  # Combine spaces and stars for the row

# print (print_triangle(5))
print (print_stars(5))