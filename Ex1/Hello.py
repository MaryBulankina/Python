value = None
# print(type(value))
# print(type(a))
# print(type(b))
value = 12334
# print(type(value))
# s = 'hello world'

# a = 123
# b = 1.23
# print(s) # вывод строки
# print(a, b, s)

# f = False
# print(f)

# list = ['1', '2', '3']
# col =['hello', 1,2,4.5,True]
# print(list)
# print(col)

# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

#Арифметические операции
# a = 1.3123312312
# b = 3
# c= round(a * b, 7)
# print(c)

# Скоращенные операции присваиания

# a = 3
# a += 5
# print(a)

#Логические операции
# a = 1 < 3 < 5 < 10  
# print(a)

# func = 1
# T = 4
# x = 123

# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

is_Odd = not f[0] % 2
print(is_Odd)

#Управляющие конструкции

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

#While

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
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(inverted)

#for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

#Срезы
# text = 'Съешь же еще этих мягких французских булок'
# print(text[0])            # с
# print(text[1])            # ъ
# print(text[len(text)])    # IndexError
# print(text[len(text)-1])  # к
# print(text[-5])           # б
# print(text[:])            # print(text)
# print(text[:])            # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9])          # ешь еще
# print(text[6:-18])        # еще этих мягких
# print(text[0:len(text):6])# сеикакл
# print(text[::6])          # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#Функции

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x ==2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))
