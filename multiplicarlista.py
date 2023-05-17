lst=[]
def multelement():
    multlista = [element * nummult for element in lst]
    print("Os resultados dos números multiplicados por",nummult,"são:",multlista)
repetir="sim"
while repetir=="sim" :
    numnum=int(input("Quantos números quer digitar? "))
    for x in range(numnum):
        lst.append(int(input("Digite um número: ")))
    nummult=int(input("Digite o número que multiplicará os inseridos anteriormente: "))
    multelement()
    repetir=input("Deseja repetir? ")
else:
    print("Fim")
    