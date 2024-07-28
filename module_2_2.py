first = int(input('Ввести первое число: '))
second = int(input('Ввести второе число: '))
third = int(input('Ввести третье число: '))
if first == second and first == third and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)