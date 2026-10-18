my_set1 = {'a','e','i','o',3.7}
#my_set2 = my_set1.union('u')
#print(my_set2)
#{'o', 'u', 3.7, 'e', 'a', 'i'}
my_set1.discard(3.7)
print(my_set1)
#{'e', 'i', 'o', 'a'}