import self


def generate_square(n):
    list = []
    for i in range(n):
        list.append('*' * n)
    return list

print(generate_square(3))



def generate_triangle(n):
    triangle = []  # List to store each row of the triangle
    for i in range(1, n + 1):  # Loop to create n rows
        triangle.append('*' * i)  # Append i stars to the list
    return triangle

# Example usage
n = 5
triangle_pattern = generate_triangle(n)

# Print the triangle pattern
for row in triangle_pattern:
    print(row)



def triangle(n):
    list3=[]
    for i in range(n):
        list3.append('*' * i)
        return list3

pattern=triangle(4)
for i in pattern:
    print(i)



class newone:
    def sum(self, a, b):
        return a+b
    def __init__(self,name,age):
        self.name= name
        self.age=age


ij=newone("john", 40)
print(ij.sum(4,3))
ij.name
print (ij.age, ij.name)
