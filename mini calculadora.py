import math

def main():
    while True:

        print("Mini calculadora de dois números: ")

        num = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))

        soma = num + num2
        mult = num * num2
        sub = num - num2

        choice = input("você deseja fazer uma soma (1), multiplicação (2) ou subtração (3)? ")
        
        if choice == "1":
            resultado = soma
        elif choice == "2":
            resultado = mult
        elif choice == "3":
            resultado = sub
        else:
            print("escolha inválida.")
            continue


        print("Resultado", resultado)

        raiz = math.sqrt(resultado)
        print("A raiz é %0.2f" %(raiz))
main()

