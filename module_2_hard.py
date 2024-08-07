num = int(input('Ввести число: '))

result = ''
for i in range(1, num):
    for j in range(i+1, num):
        if num % (i+1) == 0:
            result +=f'{i}{j}'

print(f'{num} - {result}')
