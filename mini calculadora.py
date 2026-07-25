def main():
    while True:

        print("Mini calculadora de dois números: ")

        num = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))

        choice = input("você deseja fazer uma soma (1), multiplicação (2) ou subtração (3)? ")
        
        if choice == "1":
            print(num + num2)
        elif choice == "2":
            print(num * num2)
        elif choice == "3":
            print(num - num2)
        else:
            print("escolha inválida.")
main()



