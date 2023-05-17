registros = []
filename = "equipfile.txt"
id = 0
print("********** Registro de Equipamentos **********")
escolha = ""

while escolha.lower() != "x":
    print("""Que opção pretende utilizar?
    1 - Adicionar registro
    2 - Visualizar registros
    3 - Procurar registro por nº de série
    4 - Apagar registo
    5 - Atualizar registro """)

    escolha = input("->")

    if escolha == "1":
        id += 1
        file = open(filename, "a")
        nserie = input("Digite o nº serial: ")
        marca = input("Digite a marca do equipamento: ")
        fabr = input("Digite o fabricante: ")
        tipo = input("Digite o tipo de equipamento: ")
        seg = input("Digite a data de aquisição: ")
        registro = (id, nserie, marca, fabr, tipo, seg)
        registros.append(id)
        registros.append(nserie)
        registros.append(marca)
        registros.append(fabr)
        registros.append(tipo)
        registros.append(seg)
        file.write(str(int(registro[0]))) 
        file.write("   ")
        file.write("Nº serial: ")
        file.write("   ")
        file.write(registro[1])
        file.write("   ")
        file.write("Marca: ")
        file.write(registro[2])
        file.write("   ")
        file.write("Fabricante: ")
        file.write(registro[3])
        file.write("  ")
        file.write("Equipamento: ")
        file.write(registro[4])
        file.write("  ")
        file.write("Data aquisição: ")
        file.write(registro[5])
        file.write("\n")
        file.close()
        print("------------------\n"
        "Registro adicionado.\n")
    elif escolha == "2":
        file = open(filename, 'r')
        lines = file.readlines()
        for line in lines:
             print(line.strip())
             

    elif escolha == "3":
        file = open(filename, "r")
        procura = input("Digite o nº de série do registro: ")
        lines = file.readlines()
        for line in lines:
            if line.find(procura) != -1:
                print(line)

    elif escolha == "4":
        numap = input("Digite o número de registro para apagar: ")
        with open(filename, "r") as f:
            file = f.readlines()
        with open(filename, "w") as f:
            for line in file:
                words = line.strip("\n").lower().split(' ')
            if numap.lower() not in words:
                f.write(line)
            print("Registro deletado.")

    elif escolha == "5": 
        nserieat = input("\nEscreva o  nº de série do registro que quer atualizar: ")
        for registro in registros:
            if nserieat == nserie:
                equip2 = input("Escreva o novo tipo de equipamento: ")
                with open(filename, 'r') as file :
                    file = file.read()
                filedata = file.replace(tipo, equip2)
                with open(filename, 'w') as file:
                    file.write(filedata)
                print("Registro atualizado")
                break
            else:
                print("Registro não encontrado")
             
    elif escolha.lower() == "x" or "6":
        print("Obrigada! Até á proxima.")
        break
    else:
        print("Essa opção não existe, por favor tente novamente")