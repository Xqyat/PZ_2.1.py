#2. Дано целое число N(>1). Вывести наибольшее из целых чисел K,
#для которых сумма 1+2+...+K будет меньше или равна N, и
#саму эту сумму.
my_value = 0
num= 0
try:
    N_num = int(input("Введите целое число N больше 0: "))
    while my_value <= N_num:
        num += 1
        my_value += num
    print("Сумма чисел до К: ", my_value := my_value - num)
    print("Наибольшее из целых чисел К: ", num := num - 1)
except:
    print("Введите целое число!")