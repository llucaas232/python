num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
oper=(input("Digite a operação desejada;\n"
            "1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão: "))
match oper:
    case '1':
        print("O resultado é:",num1+num2)
    case '2':
         print("O resultado é:",num1-num2)
    case '3':
            print("O resultado é:",num1*num2)
    case '4':
            print("O resultado é:",num1/num2)