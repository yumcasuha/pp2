# Пример генератора, который выдаёт числа от 1 до 5
def number_generator():
    for i in range(1, 6):
        yield i

for num in number_generator():
    print(num)

