my_dict = {'Yan': 25, 'Bruce': 31,'Oleg':18}   #словари
print(my_dict)
print(my_dict['Yan'])
print(my_dict.get('Ilya'))
my_dict.update({'Emil': 56, 'Timur': 45 })
print(my_dict)
del my_dict['Bruce']
print(my_dict)
print(my_dict.get('Bruce','Ключа нет :('))
print(my_dict)

my_set = {1,2,2,1,3,4,5,5, 'Hello', (1,2,3)}     #множества
print(my_set)
my_set.add(6)
my_set.add(7)
print(my_set)
my_set.remove(1)
print(my_set)
