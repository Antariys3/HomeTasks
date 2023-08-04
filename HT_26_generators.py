def my_generator(start, step):
    count = 0
    while count < 10:
        yield start
        start *= step
        count += 1


num = my_generator(-2, -5)
for i in num:
    print(i)
print("-" * 50)

num = my_generator(10, 3)
for i in num:
    print(i)
