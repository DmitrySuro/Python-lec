path = 'C:\Users\Пользователь\Desktop\Python\lec3\file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()


numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))

out = []

for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)
