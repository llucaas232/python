num1 = int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))
oper = int(input("Digite o operador.\n1 para adição\n2 para subtração\n3 para multiplicação\n4 para divisão: "))
if oper == 1:
    op = num1 + num2 
    print("O resultado é:",op)
if oper == 2:
    op = num1 - num2 
    print("O resultado é:",op)
if oper == 3:
    op = num1 * num2 
    print("O resultado é:",op)
if oper == 4:
    op = num1 / num2 
    print("O resultado é:",op)
else:
    print("Essa opção não existe. Tente novamente.")