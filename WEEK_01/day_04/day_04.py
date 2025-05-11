# password = input()
# confirmation = input()
# if password == confirmation:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
#
#
# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# minimum = min(a, b, c, d)
# print(minimum)
#
#
# age = int(input())
# if age <= 13:
#     print("детство")
# elif 14 <= age <= 24:
#     print("молодость")
# elif 25 <= age <= 59:
#     print("зрелость")
# else:
#     print("старость")

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')
#
# a = int(input())
#
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#
# p = (a + b) * (a + b)
# print(p)

# Ввод числа
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")