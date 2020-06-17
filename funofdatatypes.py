#assigning element to list

list1 = [1,2,3,5]
list1.insert(3,4)
list1.append(6)
print (list1)

#accessing element from tuple

tuple1 = (1,2,3,4)
print(tuple1[1])
print(tuple1[3])

#deleting element from dictionary

dict = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four"
}

del dict[3]
print(dict)
