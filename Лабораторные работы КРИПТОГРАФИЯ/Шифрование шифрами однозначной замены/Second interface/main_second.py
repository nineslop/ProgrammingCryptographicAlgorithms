import RSAa, gost_94, RSa_ds
# Основной диалог.
while True:
    action = int(input('''Выбор шифра / Выход:
1) RSA.
2) ГОСТ Р 34.10-94
3) RSA (ЭЦП).

0) Выход из программы.
Ответ пользователя:\n'''))
    
    # Обработка ввода
    if (action == 1):
        RSAa.main()
    elif (action == 2):
        gost_94.main()
    elif (action == 3):
        RSa_ds.main()
    elif action == 0:
        exit()
    print()
    hold = int(input("Продолжить работу?\n 1) Да.\n 0) Нет.\n"))
    if not hold:
      exit()
