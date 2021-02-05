months = [
    "Январь", "Февраль", "Март", "Апрель",
    "Май", "Июнь", "Июль", "Август",
    "Сентябрь", "Октябрь", "Ноябрь", "Декабрь",
]

user_input = input("Введите номер месяца: ")
if user_input.isdigit():
    if 0 < int(user_input) <= 12:
        print(f"Месяц под номером {user_input} - {months[int(user_input) - 1]}")
    else:
        print("Oops, кажется, месяца с таким номером не существует 😅")
else:
    print("Ooops, вы ввели не число 😬")