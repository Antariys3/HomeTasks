
text_1 = input("Введите текст или строку: ")
text_2 = input("Введите текст или строку: ")
text_3 = input("Введите текст или строку: ")
text_4 = input("Введите текст или строку: ")

with open("my_file.txt", "w") as file:
    file.write(text_1 + "\n")
    file.write(text_2 + "\n")

with open("my_file.txt", "a") as file:
    file.write(text_3 + "\n")
    file.write(text_4 + "\n")

