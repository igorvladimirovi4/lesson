my_dist={'Anton': 1999, 'Gleb': 2001, 'Max': 1995}
print(my_dist)
print(my_dist['Anton'])
print(my_dist.get('Gena'))
my_dist.update({'Rik': 1900,
                'Sasha': 2000})
a=my_dist.pop('Max')
print(a)
print(my_dist)

my_set={1, 2, 'one', 'two', 1, 2, 1, 1}
print(set(my_set))
my_set.add(3)
my_set.add('four')
my_set.discard(1)
print(my_set)