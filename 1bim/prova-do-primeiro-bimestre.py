
# PROVA BIMESTRAL

# Programa para gerenciar Agenda de um Chaveiro

# O sistema deve controlar apenas UM dia de trabalho ✓
# Ele realiza 12 atendimentos por dia -> for i in range(12) ✓
# Armazenar dados ANTES do menu do programa ✓

## Armazenar:

### CEP -> Int ✓
### Valor -> Float ✓
### Status 0 ou 1 -> Int ✓

# Após isso, apresente um Menu com as seguintes opções

### 1. Listar atendimentos agendados (todos status) ✓
### 2. Calcular a soma do dinheiro recebido no dia (status 1 apenas) ✓
### 3. Encontrar CEP com orçamento MAIS CARO e MAIS BARATO ✓
### 4. Sair do Programa ✓

# =================================== Listas de Dados

sql_de_pobre_cep = [0] * 12
sql_de_pobre_valor = [0] * 12
sql_de_pobre_status = [0] * 12


# =================================== Input Inicial de Dados

print('=' * 50)
print('Bem-vindo(a) ao Input do Gerenciador de Agenda!')
print('=' * 50)

for i in range(12):
    print(f'Digite o CEP do cliente nº{i+1}:')
    cep = int(input())
    sql_de_pobre_cep[i] = cep
    print(f'Digite o VALOR do serviço do cliente nº{i+1}:')
    valor = float(input())
    sql_de_pobre_valor[i] = valor
    print(f'Digite o STATUS do serviço do cliente nº{i + 1}:\n'
          f'0 = NÃO REALIZADO\n'
          f'1 = REALIZADO')
    status = int(input())
    sql_de_pobre_status[i] = status

print('=' * 50)
print(f'Tudo pronto! Você informou os seguintes dados:\n'
      f'Lista de CEPs: {sql_de_pobre_cep}.\n'
      f'Lista de VALORES: {sql_de_pobre_valor}.\n'
      f'Lista de STATUS: {sql_de_pobre_status}.')

# =================================== MENU


rodar = True
while rodar:
    print('=' * 50)
    print('Bem-vindo(a) ao Menu do Gerenciador de Agenda!')
    print('1..... Listar Atendimentos Agendados')
    print('2..... Calcular Soma do Dinheiro Recebido no Dia')
    print('3..... Encontrar CEP com orçamento MAIS CARO e MAIS BARATO')
    print('4..... Sair do Programa')
    opcao = int(input())

# =================================== Opção 1
    if opcao == 1:
        print('=' * 50)
        print('Segue a lista de Atendimentos Agendados com CEP e VALOR do serviço:')
        for i in range(12):
            print(f'Cliente Nº{i+1} | CEP: {sql_de_pobre_cep[i]} | Valor do Serviço: R${sql_de_pobre_valor[i]}')
        print('Você ira retornar ao Menu.')

# =================================== Opção 2
    if opcao == 2:
        print('=' * 50)
        print('Segue a Soma do Dinheiro Recebido no Dia (Apenas Status 1 - REALIZADO:')
        soma = 0
        for i in range(12):
            if sql_de_pobre_status[i] == 1: # se o fulano na posição i == status 1
                soma = soma + sql_de_pobre_valor[i] # o fulano na posição i de valores pode somar
        print(f'R${soma}')
        print('Você ira retornar ao Menu.')

# =================================== Opção 3
    if opcao == 3:
        print('=' * 50)
        indice_do_mais = 0
        indice_do_menos = 0
        maior_valor = 0
        menor_valor = 0
        for i in range(12):
            # "deszerando" o zero
            if i == 0:
                indice_do_mais = i
                indice_do_menos = i
                maior_valor = sql_de_pobre_valor[i]
                menor_valor = sql_de_pobre_valor[i]
            # teste maior
            if sql_de_pobre_valor[i] > maior_valor:
                maior_valor = sql_de_pobre_valor[i]
                indice_do_mais = i
            # teste menor
            if sql_de_pobre_valor[i] < menor_valor:
                menor_valor = sql_de_pobre_valor[i]
                indice_do_menos = i
        print(f'Segue o CEP com orçamento MAIS CARO:\n'
              f'CEP: {sql_de_pobre_cep[indice_do_mais]} | Valor: R${sql_de_pobre_valor[indice_do_mais]}\n'
              f'Segue o CEP com orçamento MAIS BARATO:\n'
              f'CEP: {sql_de_pobre_cep[indice_do_menos]} | Valor: R${sql_de_pobre_valor[indice_do_menos]}')
        print('Você ira retornar ao Menu.')

# =================================== Opção 4
    if opcao == 4:
        print('Você ira sair do programa agora.')
        rodar = False



# @lvcaspacifico - 04-05-2023