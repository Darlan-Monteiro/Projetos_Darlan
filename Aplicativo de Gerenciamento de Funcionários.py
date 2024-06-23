#Lista criada vazia para receber as informações dos funcionarios, e abaixo a variavel com meu RU (ID)
lista_funcionario = []
id_global = 4892756

#Aqui estamos pegando os daDos dos funcionarios e adicionando a lista
def cadastrar_funcionario(id):
    print('\n\n  --------------------------\n','      MENU DE CADASTRO      \n',' --------------------------\n',f'| ID: {id_global}')
    nome = str(input(' | Digite o nome completo: '))
    setor = str(input(' | Digite o setor: '))
    salario = float(input(' | Digite o salário: '))
    funcionario = {'ID': id, 'Nome': nome, 'Setor': setor, 'Salário': salario}
    lista_funcionario.append(funcionario.copy())

#aqui eu criei para fazer uma saida mais organizada
def formatar_funcionario(funcionario):
    return (f"\nID: {funcionario['ID']}\n"
            f"Nome: {funcionario['Nome']}\n"
            f"Setor: {funcionario['Setor']}\n"
            f"Salário: {funcionario['Salário']}\n")

#consultando os funcionarios cadastrados
def consultar_funcionario():
    while True:
        try:
            consulta = int(input('\n\n--------------------------\n'
                                 '|        CONSULTA        |\n'
                                 '--------------------------\n'
                                 '| 1. Consultar Todos     |\n'
                                 '| 2. Consultar por ID    |\n'
                                 '| 3. Consultar por Setor |\n'
                                 '| 4. Retornar ao menu    |\n'
                                 '  Digite a opção desejada: '))
        except ValueError:
            print('\nOpção inválida. Por favor, digite um número inteiro.')
            continue
            
        
        if consulta == 1:
            for i in lista_funcionario:
                print(formatar_funcionario(i))
        elif consulta == 2:
            try:
                id_fun = int(input('\n| Digite o ID do funcionário: '))
            except ValueError: #adicionei para caso o usuario não insira um valor inteiro
                print('\nOpção inválida. Por favor, digite um número inteiro.')
                continue
            for id_func in lista_funcionario:
                 if id_func['ID'] == id_fun:
                    print(formatar_funcionario(id_func))
                    break

        elif consulta == 3:
            csetor = str(input('\n| Digite o setor'))
            for cont_setor in lista_funcionario:
                if cont_setor['Setor'] == csetor:
                    print(formatar_funcionario(cont_setor))

        elif consulta == 4:
            return
        else:
            print('\nOpção inválida.')
                
#aqui pego o id que será removido e vejo se está na lista para que o sistema delete            
def remover_funcionario():
    try:
        id_remover = int(input('\n| Digite o ID: '))
    except ValueError:
        print('\nID inválido. Por favor, digite um número inteiro.')
        return
    

    for funcionario in lista_funcionario:
        if funcionario['ID'] == id_remover:
            lista_funcionario.remove(funcionario)
            print(f'Funcionário com ID {id_remover} removido com sucesso')
   
            break


                
            
#aqui o menu principal     
while True:
    try:

        menu = int(input('\n\n Bem-Vindo a loja do Darlan\n'
                         '--------------------------\n'
                         '|           MENU           |\n'
                         '--------------------------\n'
                         '| 1. Cadastrar Funcionário |\n'
                         '| 2. Consultar Funcionário |\n' 
                         '| 3. Remover Funcionário   |\n'
                         '| 4. Sair                  |\n'
                         '  Digite uma opção: '))
    except ValueError:
            print('\nOpção inválida. Por favor, digite um número inteiro.')#adicionei para caso o usuario não insira um valor inteiro
            continue
    if menu == 1:
        id_global += 1
        cadastrar_funcionario(id_global)
    elif menu == 2:
        consultar_funcionario()
    elif menu == 3:
        remover_funcionario()
    elif menu == 4:
        break
    else:
        print("Opção inválida")
