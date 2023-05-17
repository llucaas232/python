class cliente:
    def __init__(self, data, nome, tel, tarefa, obs):
        self.__data = data
        self.__nome = nome
        self.__tel = tel
        self.__tarefa = tarefa
        self.__obs = obs
        
    def set_data(self, data):
        self.__data = data
    def set_nome(self, nome):
        self.__nome = nome
    def set_tel(self, tel):
        self.__tel = tel
    def set_tarefa(self, tarefa):
        self.__tarefa = tarefa
    def set_obs(self, obs):
        self.__obs = obs

    def get_data(self):
        return self.__data
    def get_nome(self):
        return self.__nome
    def get_tel(self):
        return self.__tel
    def get_tarefa(self):
        return self.__tarefa
    def get_obs(self):
        return self.__obs

    def __str__(self):
        return "Data: " + str(self.__data) + \
            ", Nome do cliente: " + str(self.__nome) + \
            ", Número de telemóvel:"+ str(self.__tel) + \
            ", Tarefa: " + str(self.__tarefa) + \
            ", Observações: " + str(self.__obs) 


clientes=[]
n = int(input('Quantos registros quer inserir? '))
for i in range(n):
    data = input('Digite a data: ')
    nome = input('Insira o nome do cliente: ')
    tel = int(input('Insira o número de telemóvel do cliente: '))
    tarefa = input('Digite a tarefa: ')
    obs = input('Digite as observações: ')
    print()
    cliente = cliente(data, nome, tel, tarefa, obs)
    clientes.append(cliente)  



print('Detalhes dos clientes:\n')
for cliente in clientes:
    print('Data: ', cliente.get_data())
    print('Nome do cliente: ', cliente.get_nome())
    print('Número de telemóvel: ', cliente.get_tel())
    print('Tarefa: ', cliente.get_tarefa())
    print('Observações: ', cliente.get_obs())
    print()


nome = input('\nEscreva o nome do cliente que quer apagar: ')
for cliente in clientes:
    if cliente.get_nome() == nome:
        clientes.remove(cliente)
        print('Registro apagado')
        break
else:
    print('Registo não encontrado')



nome = input('\nEscreva o nome do cliente que quer atualizar: ')
for cliente in clientes:
    if cliente.get_nome() == nome:
        alt = input('Escreva ao que será alterado (tarefa ou data): ')
        if alt == "tarefa":
            taralt = input('Escreva a nova tarefa: ')
            cliente.set_tel(taralt)
            print('Registo atualizado')
            break
        if alt == "data":
            datalt = input('Escreva a nova data: ')
            cliente.set_mat(datalt)
            print('Registo atualizado')
            break
else:
    print('Registo não encontrado')

