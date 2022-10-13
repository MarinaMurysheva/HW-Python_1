x = int(input('Введите x: '))
y = int(input('Введите y: '))

if x == 0 or y == 0:
    print('x и y не могут быть равны нулю')
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')