

def digit_recognition(text: str):
    #  проверка на все возможные исключения(число ли это, "-", ",", ".")
    if not text.replace(',', '').replace('.', '').replace('-', '').isdigit() \
            or text.count('-') > 1 or text.replace(',', '.').count('.') > 1:
        return "Вы ввели не корректное число: " + text
    else:
        #  проверяем на ноль, дробный ноль и если ноля нет перед точкой
        if text.startswith("0") and len(text) == 1:
            return "Вы ввели ноль"
        elif str(float(text.replace(',', '.'))) == "0.0":
            return "Вы ввели ноль"
        else:
            #  проверки на положительное и дробное число
            number = "Вы ввели "
            if text.startswith("-"):
                number += "отрицательное "
            else:
                number += "положительное "
            if text.replace(',', '.').count('.'):
                number += "дробное "
                #  Доп. задание если перед точной нет ноля
                text = str(float(text.replace(',', '.')))
            else:
                number += "целое "
            # в number собираем все возможные результаты(кроме ноля)
            return number + "число: " + text.replace(',', '.')


while True:
    user_input = input("Введите число: ")
    if user_input.lower() in ["выход", "exit", "quit", "e", "q"]:
        break
    else:
        print(digit_recognition(user_input))
