
# path = 'C:\Users\Пользователь\Desktop\Python\lec3\file.txt'
# f = open('file.txt', 'r')
# data = f.read() + ' '
# f.close()


# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))

# out = []

# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)


data = '1 2 3 5 8 15 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)


# li = [x for x in range(1,21)]

# li = list(map(lambda x:x+10,li))

# print(li)

# data = list(map(int,'1 2 3 4'.split()))

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)
