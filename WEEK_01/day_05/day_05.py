# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or b == c or a == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")


a = int(input())
b = int(input())
c = int(input())
# Помещаем числа в список, сортируем и выводим средний элемент
numbers = [a, b, c]
numbers.sort()
print(numbers[1])


color1 = input()
color2 = input()

primary_colors = {"красный", "синий", "желтый"}

if color1 not in primary_colors or color2 not in primary_colors:
    print("ошибка цвета")
elif color1 == color2:
    print(color1)
elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
    print("оранжевый")
elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
    print("зеленый")

# Чтение входных данных
age = int(input())  # возраст
gender = input()  # пол (мужчина или женщина)

# Проверка условий для вступления в команду
if 10 <= age <= 15 and gender == 'f':
    print("YES")
else:
    print("NO")


# Словарь для сопоставления чисел и римских цифр
roman_numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}

# Чтение входного числа
num = int(input())

# Проверка на допустимость числа и вывод соответствующего результата
if 1 <= num <= 10:
    print(roman_numerals[num])
else:
    print("ошибка")
