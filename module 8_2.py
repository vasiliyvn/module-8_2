
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers: #Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
        try:
            result+=number
            #Если же при переборе встречается данное типа отличного от числового,
            # то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы {number}')
            incorrect_data += 1
    return result,incorrect_data #В конечном итоге функция возвращает кортеж из двух значений:
def calculate_average(numbers):
    #Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее
    try:
        result = personal_sum(numbers)
        res = result[0]/(len(numbers)-result[1])
        return res
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать