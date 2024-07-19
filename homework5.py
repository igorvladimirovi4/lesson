immutable_var = (1, 'two', 3, 'four')
print(immutable_var)

immutable_var[0] = 100
print(immutable_var)
# обращение по элементам кортеж не поддерживает

mutable_list = ['one', 'two', 3, 4]
mutable_list[0] = 1
print(mutable_list)
