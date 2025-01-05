def generate_square1(n):
    list1 = []
    for i in range(1,n+1):
        list1.append('*' * (i ** n))
        print
    return list1

print(generate_square1(3))

def triangle(n):
    list3=[]
    for i in range(1,n+1):
        list3.append('*' * i)
    return list3


pattern = triangle(3)

for i in pattern:
    print(i)

# def generate_triangle(n):
#     triangle = []  # List to store each row of the triangle
#     for i in range(1, n + 1):  # Loop to create n rows
#         triangle.append('*' * i)  # Append i stars to the list
#     return triangle
#
# # Example usage
# n = 5
# triangle_pattern = generate_triangle(n)
#
# # Print the triangle pattern
# for row in triangle_pattern:
#     print(row)

def invert_triangle(n):
    list4=[]
    for i in range(n,0,-1):
        list4.append('*' * i)
    return list4


pattern1 = invert_triangle(8)

for i in pattern1:
    print(i)