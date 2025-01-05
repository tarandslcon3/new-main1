empyt_dict={}

student={'name':'krish', 'age':32, 'grade':3.2}
print(student)
kes=student.keys()
print(kes)
sqrlst=[]
for x in range(10):
    x = x**2
    if x%2 == 0:
        sqrlst.append(x)
print(f"even square:{sqrlst}")

evens={x:x**2 for x in range(10) if x%2==0}
print(evens)

numbers=[1,2,3,3,4,5,4,5,6,7,4,3,2,2,4,5,6,7,8,9,0,1,2,0,0]
#count frequency of numbers using dic
frequency={}

for i in numbers:
    if i in frequency:
        # frequency[i] +=1
        frequency[i] =+ 1
    else:
        frequency[i]=1
print(frequency)

dict1={'a':'adad', 'b':3, 'c':'dad'}
dict2={'d':'dadad', 'e':32, 'f':'2dad'}
dict3={**dict1,**dict2}
print(dict3)

for i,v in dict3.items():
    if isinstance(v,int):
        print(f'{i}: {v}')


tuple1 =(1,2,3,4,2,232,42,1,0,1,1,0,33,4,4,5,5,6,6,7,7,0,2,2,4)

frequency={}
for i in tuple1:
    if i in frequency:
        # frequency[i] +=1
        frequency[i] += 1
    else:
        frequency[i]=1
print(frequency)

tuple2=tuple1*3
print(tuple2)

frequency={}
for i in tuple2:
    if i in frequency:
        # frequency[i] +=1
        frequency[i] += 1
    else:
        frequency[i]=1
print(frequency)

list1 = [1,2,3,4,5,6,4,2,4,30,9,0,9,0,8,2,6,5,4,3,1,4,56,0]
list1[0]=4
print(list1)

tuple4=1,2,3,4,'rsdf'
print(tuple4)

a,b,c,d,e=tuple4
print (a)
print (5)




