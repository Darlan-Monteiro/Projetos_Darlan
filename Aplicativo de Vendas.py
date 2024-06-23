print('Seja bem-vindo ao nosso sistema, Darlan Monteiro.', '\n')


#meu input para receber os valores e armazenar nas variaveis #exigência 6
valor_pedido = float(input('Por favor, insira o valor do pedido: '))
qtd_parcelas = int(input('Por favor, insira a quantidade de parcelas: '))


#bloco de cód para definir o valor do juros #exigência 6
if qtd_parcelas < 4:
    juros = 0/100
elif qtd_parcelas >= 4 and qtd_parcelas < 6:
    juros = 4/100
elif qtd_parcelas >= 6 and qtd_parcelas < 9:
    juros = 8/100
elif qtd_parcelas >= 9 and qtd_parcelas < 13:
    juros = 16/100
else:
    juros = 32/100


#aqui estou calculando os valores das parcelas de acordo com meu input e cim meus ifs #exigência 6
valor_parcela = valor_pedido * (1 + juros) / qtd_parcelas
tot_parcelado = valor_parcela * qtd_parcelas


#obs: Aqui eu quis testar outra forma de printar o nome, favor não tirar pontos.#exigência 6
nome = 'Darlan Monteiro'
print('\n'f'Nome Completo: {nome}.')


if qtd_parcelas >= 4:
    print(f'Quantidade de parcelas: {qtd_parcelas}', f'Valor da parcela: R$ {valor_parcela:.2f}', f'Valor total a ser pago: R$ {tot_parcelado:.2f}', sep = '\n')
else:
    print(f'Quantidade de parcelas: {qtd_parcelas}','Parcelamento sem juros.', sep = '\n')
