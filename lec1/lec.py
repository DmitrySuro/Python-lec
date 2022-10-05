

# типы данных и переменная
# int, float, boolean, str, list, None


#value = None
# print(type(value))

#a = 123
#b = 1.23
# print(type(a))
# print(type(b))
#value = 12334
# print(type(value))

#s = 'hello world'
# print(s) # вывод строки

#print(a, '-', b, '-', s)
#print('{1} - {2} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#f = True
# print(f)

#list = ['1', '2', '3']
#col = ['hello', 1, 2, 3, 4.5, True]
# print(col)
# print(list)
#print('Введите а')
#a = float(input())
#print('Введите b')
#b = float(input())
#print(a, ' + ', b, ' = ', a+b)
#print('{} {}' .format(a, b))
#print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
#
# (),Сокращенные операции
#a = 1.3123
#b = 3
#c = round(a * b, 5)
# print(c)

# a = 3
# a += 5
# print(a)


# Логические операции
# >, >=, <, <=, == ,!=
# not, and, or - не путать с &, |, ^
# is, is not, in, noy in
# gen

# a = 1 == 2
# print(a)
# func =1
# t= 3
# x = 123

# print(func<t>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]

# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Управляющие конструкции
# while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)

# Управляющие конструкции
# for

# list = [1,2,7,3,4,5]

# for i in list:
#     print(i)


# for i in range(1, 10, 2):
#     print(i)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return