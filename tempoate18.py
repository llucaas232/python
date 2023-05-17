from datetime import date
hoje=date.today()
nome=input("Digite seu nome: ")
anonasc=int(input("Digite seu ano de nascimento: "))
mesnasc=int(input("Digite seu mês de nascimento: "))
dianasc=int(input("Digite seu dia de nascimento: "))
aniver=date(anonasc,mesnasc,dianasc)
idade=(hoje-aniver)
idaf=int((idade.days/365))               
if int(idaf)<18:
    dezoito=int(input("Digite o ano em que fará 18 anos: "))
    data2=date(dezoito,mesnasc,dianasc)
    diasate=(data2-hoje)
else:
    print("O programa não pode ser continuado. O usuário precisa ter menos de 18 anos de idade.")
print("O seu nome é",nome+". Seu aniversário é em",aniver,"e você tem",idaf,"anos.\n"
"Você fará 18 anos em",diasate.days,"dias.")