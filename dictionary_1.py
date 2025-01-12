dictionary23={"name":["taran","rahul", "test1"], "area":["toronto", "brantford","hamilton"]}
print (dictionary23.items().capitalize())
print(dictionary23["name"][0])
print(dictionary23["name"][0].capitalize())

def captilaize_dic(dic):
    for i in dic:
        dic[i] = [value.capitalize() for value in dic[i]]
    return dic

test1 =captilaize_dic(dictionary23)
print(test1)

dictionary_1={"name"}
