my_dict={'Misha':2030,'Vasya':2020,'Alesha':2010,'Petya':2000}
print(my_dict)
print(my_dict['Petya'])
print(my_dict.get('Petya'))
print(my_dict.get('Egor'))
my_dict.update({'Egor':1990,'Stas':1980})
deleted = my_dict.pop('Alesha')
print(deleted)
print(my_dict)

my_set={4,8,'lost',1,5,'lost',1,6,True,2,3,True,4,2}
print(my_set)
my_set.add(9)
my_set.add(10)
my_set.discard(1)
print(my_set)

