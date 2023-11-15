# a) criar uma função abrirorcamento() que devera dentro do codigo
# solicitar os dados de UM UNICO orçamento (numero de telefone, valor total, status 1 ou 2)
    # quando o usuário do programa digitar a opção 1 a função abrir sera chamada
    # armazenar as listas globais na proxima posição livre

# b) criar uma função orcamentomaiscaro() essa função pesquisa pelo orçamento com valor total
# mais alto e então retorna como resultado da função o numero do tel do cliente
    # quando o user digitar 2 a função orcamais devera ser chamada

# c) criar uma função contarorcamentos(Status:int), essa funcao devera contar
# e mostrar em tela quantos orçamentos tem o status igual ao recebido pelo parametro de entrada
# da função
    # quando o user  digitar a opção 3 devera contar e mostrar em tela quantos orçamentos tem status
    # igual ao recebido pelo parametro de entrada da função

# quando o usuário digitar a opção 4 devera encerrar o programa

# status 1 = Pendente
# status 2 = Aprovado pelo Cliente

# CONTROLE DE ORÇAMENTOS
# 1... Registrar orçamento
# 2... Mostrar orçamento mais caro
# 3... Contar orçamentos
# 4... Sair do programa


sql_de_pobre_telefones = [0] * 4
sql_de_pobre_valores = [0] * 4
sql_de_pobre_status = [0] * 4


def abrirorcamento():
    index = 0
    contador = 0
    livre = False
    while not livre:
        if contador == 4:
            print('Limite máximo de registros excedido! :(')
            break
        if sql_de_pobre_status[contador] == 0 and contador < 4:
            index = contador
            livre = True
        contador += 1
    if contador < 4:
        sql_de_pobre_status[index] = int(input(f'Digite o status do orçamento:\n'
                                                      f'1.... Pendente\n'
                                                      f'2.... Aprovado pelo Cliente\n'))
        sql_de_pobre_valores[index] = float(input(f'Digite o valor em reais do orçamento:\n'
                                                  f'R$'))

        sql_de_pobre_telefones[index] = int(input(f'Digite o número de telefone do cliente:\n'))


def orcamentomaiscaro():
    o_mais_caro = 0
    valor_o_mais_caro = 0
    for i in range(4):
        if sql_de_pobre_status[i] != 0:
            if sql_de_pobre_valores[i] > valor_o_mais_caro:
                valor_o_mais_caro = sql_de_pobre_valores[i]
                o_mais_caro = i
    return f'Seguem dados do orçamento mais caro:\n' \
           f'Telefone: {sql_de_pobre_telefones[o_mais_caro]}'


def contarorcamentos(status:int):
    total_status = 0
    for i in range(4):
        if sql_de_pobre_status[i] == status:
            total_status += 1

    print(f'Total de orçamentos com status informado é {total_status}')
    print('=' * 40)


opcao = 0
while opcao != 4:
    print('=' * 40)
    print(f'Controle de Orçamentos\n'
          f'1.... Registrar orçamento\n'
          f'2.... Mostrar orçamento mais caro\n'
          f'3.... Contar os orçamentos por status\n'
          f'4.... Sair do programa')
    if opcao != 4:
        opcao = int(input('Digite o número da opção escolhida:'))
        print('=' * 40)

    if opcao == 1:
        abrirorcamento()

    if opcao == 2:
       print(orcamentomaiscaro()) # Como o enunciado pediu pra retornar usei return, podia ter usado print direto na função e só chamar ela

    if opcao == 3:
        status_pesquisa = (int(input(f'Digite o número do status que deseja consultar:\n'
                                    f'1.... Pendente\n'
                                    f'2.... Aprovado pelo Cliente')))
        contarorcamentos(status_pesquisa)

    # checando a gravação nas listas
    # print(f'Base de Status: {sql_de_pobre_status}\n'
    #      f'Base de Telefones:{sql_de_pobre_telefones}\n'
    #      f'Base de Valores: {sql_de_pobre_valores}')

# Fim! @lvcaspacifico | Lucas Reinaldo Pacífico | 06/07/2023 | ALPC II




