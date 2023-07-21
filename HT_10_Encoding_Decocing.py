
text = b'r\xc3\xa9sum\xc3\xa9'
text_str = text.decode()
print("Декодированый результат:", text_str)

text_latin1 = text_str.encode("Latin1")
print("Кодировка Latin1:", text_latin1)

text_str = text_latin1.decode("Latin1")
print("Декодированый результат из Latin1:", text_str)
