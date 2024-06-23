print('Seja bem-vindo(a) ao nosso sistema, Darlan Monteiro.','\n')
print(' -------------------------Cardápio------------------------','\n','| Tamanho |','| Bife Acebolado(BA) |','| Filé de Frango(FF) |')
print(' |    P    |','|    R$ 16.00        |','|    R$ 15.00        |','\n',
      '|    M    |','|    R$ 18.00        |','|    R$ 17.00        |','\n',
      '|    G    |','|    R$ 22.00        |','|    R$ 21.00        |' )
print(' ---------------------------------------------------------')


cont_valor = 0


while True:

#inputs para receber a info do usuario e verificar se bate com o cardápio.
#usei upper para deixar o texto do input todo maiúsculo, para prever possiveis erros no código
    
    sabor = str(input('Digite o sabor BA para Bife Acebolado ou FF para Filé de Frango: '))
    sabor = sabor.upper()
    if sabor != "BA" and sabor != "FF":
        print('Sabor inválido. Tente novamente')
        continue
        

    tamanho = str(input('Digite o tamanho P para Pequeno, M para Médio e G para Grande: '))
    tamanho = tamanho.upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print('Tamanho inválido. Tente novamente')
        continue

#aqui eu verifico o sabor e o tamanho para definir um valor e add no contador
    if sabor == "BA":
        if tamanho == "P":
            print('Você pediu um Bife Acebolado no tamanho P no valor de: R$ 16.00','\n')
            cont_valor += 16
        elif tamanho == "M":
            print('Você pediu um Bife Acebolado no tamanho M no valor de: R$ 18.00','\n')
            cont_valor += 18
        else:
            print('Você pediu um Bife Acebolado no tamanho G no valor de: R$ 22.00','\n')
            cont_valor += 22
            
    if sabor == "FF":
        if tamanho == "P":
            print('Você pediu um Filé de Frango no tamanho P no valor de: R$ 15.00','\n')
            cont_valor += 15
        elif tamanho == "M":
            print('Você pediu um Filé de Frango no tamanho M no valor de: R$ 17.00','\n')
            cont_valor += 17
        else:
            print('Você pediu um Filé de Frango no tamanho G no valor de: R$ 21.00','\n')
            cont_valor += 21

    
    outro_desejo = str(input('Deja pedir mais alguma coisa? SIM/NÃO: '))
    outro_desejo = outro_desejo.upper()
    if outro_desejo == "NÃO" or outro_desejo == "NAO":
        
        break
        
            
print('O valor do pedido foi de: R$ {:.2f}'.format(cont_valor))
