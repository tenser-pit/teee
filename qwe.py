from random import randint

# Задаём нулевое значение счётчику попыток
i = 0
# счётчику подбрасываний
x = 0
# и общему числу подбрасываний
all_tries = 0


# Осуществляем 10 попыток. В одном цикле будет 1 попытка
for j in range(0, 10):
    # Задаём переменной result значение пустой строки
    result = ''

    # Осуществляем 3 первых подбрасывания. В одном цикле 1 подбрасывание
    for i in range(0, 3):
        o_or_r = randint(0, 1)

        if o_or_r == 1:
            coin_value = 'О'
        else:
            coin_value = 'Р'

        result += coin_value

        i += 1

    # Осуществляем остальные подбрасывания. В одном цикле 1 подбрасывание
    while result[-1] != result[-2] or result[-1] != result[-3] or result[-2] != result[-3]:
        o_or_r = randint(0, 1)

        coin_value = 'O' if o_or_r == 0 else 'P'
        # if o_or_r == 1:
        #     coin_value = 'О'
        # else:
        #     coin_value = 'Р'

        result += coin_value

        i += 1

    # Выводим кол-во подбрасываний
    print(result, f" (кол-во подбрасываний: {i})")

    # Считаем общее кол-во попыток
    all_tries += i
    # и подбрасываний
    x += 1


# Вычисляем среднее количество подбрасываний
average_number_of_tries = all_tries / x

# Выводим результат
print(f"Среднее количество подбрасываний: {average_number_of_tries}.")