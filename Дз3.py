# Представьте, что вы хотите создать симуляцию банковского счета, где пользователь может внести или снять
# деньги и проверить баланс. Счет закрывается, если баланс становится отрицательным.
# startwork = input("Хотите начать работу с вашим банковским счетом?(да/нет)")
# каждый раз запрашивать PIN-код
balance = 0
startwork = ""
while startwork.lower() != "нет":
    ask = input("Хотите внести или снять деньги с вашего счета?(внести/снять)")
    if ask.lower() == "внести":
        increase = int(input("Введите сумму которую хотите внести..."))
        balance += increase
        print("Теперь на вашем счету:", balance, "рублей")
    else:
        decrease = int(input("Введите сумму которую вы хотите снять"))
        balance -= decrease
        print("Теперь на вашем счету:", balance, "рублей")
        if balance < 0:
            print("У вас отрицательный счет! Ваш счет был закрыт.")
            break
    startwork = input("Хотите начать работу с вашим банковским счетом?(да/нет)")
