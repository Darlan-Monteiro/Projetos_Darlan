import pandas as pd

# Função para login
def login():
    user_senha = pd.read_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\login.csv', sep=';')
    print("| ------------------------- |")
    print("| BEM-VINDO(A) AO NOBANK'S! |")
    print("| ------------------------- |")
    
    while True:
        try:
            global user #transformando em uma variável global
            user = int(input('* Digite o usuário: '))
            
        except:
            print('\nOpção inválida, utilize somente números. Por favor, tente novamente.\n')
            continue
            
        global senha 
        senha = input('* Digite a senha: ')

        
            
            # Verifica se a combinação de usuário e senha existe na base de dados
        
        if ((user_senha['Usuário'] == int(user)) & (user_senha['Senha'] == senha)).any():
            print('Login efetuado\n')
            break
            
        elif user == '' or senha == '':
            break
            
        else:
            print('\nUsuário ou senha incorretos, tente novamente.\n')



# Função para saldo
def saldo():
    user_saldo = pd.read_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';')
    user_saldo_linha = user_saldo[user_saldo['Usuário'] == int(user)] #esta verificando se é verdade se user contém na coluna usuario
    
    if not user_saldo_linha.empty: #se não estiver vazio faça
        tot_saldo = user_saldo_linha['Saldo'].values[0] #dado armazenado no vetor e sendo salvo na variavel
        
    else:
        tot_saldo = 0.0      
    print(' - Saldo: R$ {:.2f}\n'.format(tot_saldo))
    
    

# Função para deposito    
def deposito():
    user_deposito = pd.read_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';')
    user_deposito_coluna = user_deposito[user_deposito['Usuário'] == int(user)]
    
    if not user_deposito_coluna.empty:
        tot_deposito = user_deposito_coluna['Saldo'].values[0]
        
    else:
        tot_deposito = 0.0
        
    while True:
        
        valor = float(input('Digite o valor de depóstio: '))
        
        if valor > 5000:
            print('\nO valor é superior ao limite de R$ 5.000. Tente novamente\n')
            
        else:
            confimacao = input('Deseja continuar? SIM/NÃO: ').upper().strip()
            
            if confimacao == 'SIM' or confimacao == 'S':
                tot_deposito += valor
#loc aqui está verificando se a coluna usuario contem o user, então ele vai na linha que tem e acessa a coluna saldo,_
#então a linha da coluna saldo está recebtndo tot_saldo.
                user_deposito.loc[user_deposito['Usuário'] == int(user), 'Saldo'] = tot_deposito
                user_deposito.to_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';', index = False)
                print('\nDepósito concluído com sucesso.\n')
                break
                
            else:
                print('\nDepósito cancelado.\n')
                break



# Função para saque                
def saque():
    user_saque = pd.read_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';')
    user_saque_coluna = user_saque[user_saque['Usuário'] == int(user)]
    
    if not user_saque_coluna.empty:
        tot_saque = user_saque_coluna['Saldo'].values[0]
        
    else:
        tot_saque = 0.0

    while True:
        
        valor = float(input('Digite o valor de saque: '))
        
        if valor > 5000:
            print('\nO valor é superior ao limite de R$ 5.000. Tente novamente\n')
            
        elif valor > tot_saque:
            print('\nSaldo insuficiente\n')
            
        else:
            confimacao = input('Deseja continuar? SIM/NÃO: ').upper().strip()
            
            if confimacao == 'SIM' or confimacao == 'S':
                tot_saque -= valor
                user_saque.loc[user_saque['Usuário'] == int(user), 'Saldo'] = tot_saque
                user_saque.to_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';', index= False)
                print('\nSaque concluído com sucesso\n')
                break
                
            else:
                print('\nSaque cancelado.\n')
                break



# Função para transferência
def transferencia():
    user_transferencia = pd.read_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';')
    user_transferencia_coluna = user_transferencia[user_transferencia['Usuário'] == int(user)]
    
    if not user_transferencia.empty:
        tot_transferencia = user_transferencia_coluna['Saldo'].values[0]       
    else:
        tot_transferencia = 0.0
    while True:   
        destinatario = int(input('Digite o usário destinatário: '))    
        if destinatario not in user_transferencia['Usuário'].values:
            print('\nUsuário não encontrado\n')     
        else:
            valor = float(input('Digite o valor para transferência: '))   
            if valor > 5000:
                print('\nO valor é superior ao limite de R$ 5.000. Tente novamente.\n')            
            elif valor > tot_transferencia:
                print('\nSaldo insuficiente\n')         
            else:
                confirmacao = input('Deseja confirmar? SIM/NÃO: ').upper().strip()    
                if confirmacao == 'SIM' or confirmacao == 'S':
                    tot_transferencia -= valor
                    user_transferencia.loc[user_transferencia['Usuário'] == int(user), 'Saldo'] = tot_transferencia
                    user_transferencia.loc[user_transferencia['Usuário'] == destinatario, 'Saldo'] += valor
                    user_transferencia.to_csv(r'C:\Users\SAMSUNG\Downloads\projeto banco\infos.csv', sep=';', index=False)
                    print('\nTransferência concluída com sucesso\n')
                    break   
                else:
                    print('\nTransferência cancelada.\n')
                    break
login()
while True:

    try:
        menu = int(input(
                         '---------------------\n'
                         '|       MENU        |\n'
                         '---------------------\n'
                         '| 1. SALDO          |\n'
                         '| 2. DEPÓSITO       |\n' 
                         '| 3. SAQUE          |\n'
                         '| 4. TRANSFERÊNCIA  |\n'
                         '| 5. SAIR           |\n'
                         '  Digite uma opção: '))     
    except ValueError:
        print('\nOpção inválida. Por favor, digite um número inteiro.\n') #adicionei para caso o usuario não insira um valor inteiro
        continue
        
    if menu == 1:
        saldo()
        
    elif menu == 2:
        deposito()
        
    elif menu == 3:
        saque()
        
    elif menu == 4:
        transferencia()
        
    elif menu == 5:
        break
        
    else:
        print('\nOpção inválida.\n')
                