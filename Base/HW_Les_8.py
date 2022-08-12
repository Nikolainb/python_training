
s = 0
while True:
    v = input('Введите данные: ')
    if v == "sum":
        print("Общая сумма: ", s)
        s = 0
        continue
    elif v == "exit" or v == "quit":
        break
    s = s + int(v) # s += int(v)