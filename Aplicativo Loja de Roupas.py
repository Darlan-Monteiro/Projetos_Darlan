print('Bem-Vindos a Storekits')

#aqui tenho minha função para definição dos valores do modelo
def escolha_modelo():
    while True:
        modelo = input('---------------------------------------\n'
                        'Temos os seguintes modelos em estoque:\n'
                       '------------------------------------------\n'
                        '| Camiseta Manga Curta Simples (MCS)     |' 
                        '\n| Camiseta Manga Longa Simples (MLS)     |' 
                        '\n| Camiseta Manga Curta Com Estampa (MCE) |'
                        '\n| Camiseta Manga Longa Com Estampa (MLE) |\n'
                       '------------------------------------------\n'
                        '\nDigite o código do modelo MCS/MLS/MCE/MLE: ').upper().strip()
        
        if modelo == 'MCS':
            valor = 1.80
            return valor
        elif modelo == 'MLS':
            valor = 2.10
            return valor
        elif modelo == 'MCE':
            valor = 2.90
            return valor
        elif modelo == 'MLE':
            valor = 3.20
            return valor

        else:
            print("Opção inválida. Tente novamente.")
modelo_valor = escolha_modelo() #chamando a minha função

#aqui tenho minha função para definição do desconto caso haja
def ncamisas():
    while True:
        try:
            qtdcamisas = int(input('------------------------------------------\n'
                                   "\nDigite a quantidade de camisas: "))
            if qtdcamisas > 20000:
                print("Quantidade inválida de camisas. Deve ser entre 1 e 20000.")
                continue
            elif qtdcamisas < 20:
                return qtdcamisas
            elif 20 <= qtdcamisas < 200:
                return qtdcamisas * (5/100)
            elif 200 <= qtdcamisas < 2000:
                return qtdcamisas * (7/100)
            elif 2000 <= qtdcamisas <= 20000:
                return qtdcamisas * (12/100)
        except:
            print("Quandidade inválida. Não utilize virgulas, pontos, letras ou outros caracteres.\n Digite um NÚMERO INTEIRO.")
desconto = ncamisas() #chamando a minha função          
            
#verifico o tipo de frete aqui  
def frete():
    while True:
        try:
            frete = int(input('------------------------------------------\n\n'
                              'Formas de Envio/Retirada: \n'
                              '0 - Retirar pedido: Grátis \n' 
                              '1 - Tranportadora: R$ 100,00 \n'
                              '2 - Sedex: R$ 200 \n'                             
                              'Insira uma das opções: '))
            if frete == 0:
                totfrete = 0
            elif frete == 1:
                totfrete = 100
            elif frete == 2:
                totfrete = 200
            
                
            return totfrete
        except:
            print("Opção inválida. Não utilize virgulas, pontos, letras ou outros caracteres.\nDigite um NÚMERO INTEIRO.\n")
frete = frete() #chamando a minha função

total_pagar = (modelo_valor * desconto) + frete

print('\nObrigado por comprar na Storekits!\n','O valor total das sua compra foi de: R$ {:.2f}'.format(total_pagar))
