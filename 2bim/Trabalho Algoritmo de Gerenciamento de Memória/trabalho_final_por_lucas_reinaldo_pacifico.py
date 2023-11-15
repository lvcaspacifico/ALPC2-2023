import random

# ================================================== Declarando Variáveis
memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''

# ================================================== Gerando a Memória
for i in range(100):
    if (random.randint(0, 11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

# ================================================== Printando a Memória
flag_pular_linha = 20
tamanho_linha = 20

for i in range(100):
    if i < (flag_pular_linha - 1):
        print(memoria[i], end=' | ')
    else:
        print(memoria[i], end=' |\n', )
        flag_pular_linha += tamanho_linha

# ================================================== Separador
print('=' * 100)

# ================================================== Menu de Usuário
opcao = 0
while (opcao != 4):
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero:")
    opcao = int(input())
    # Só pedir inputs se não tiver pedido pra sair
    if opcao != 4:
        print("Digite o tamanho da informação:")
        tamanho = int(input())
        print("Digite a letra a ser gravada:")
        letra = input()

# ================================================== Primeira Opção
    if (opcao == 1):
        print(f'Opção Selecionada: 1 - Primeira Escolha\n'
              f'"Sua informação {letra} de tamanho {tamanho} será armazenada no PRIMEIRO espaço disponível."')
        contando_vazio = 0
        i = 0
        while True:
            if memoria[i] == ' ':
                contando_vazio += 1
            if memoria[i] != ' ':
                contando_vazio = 0
            if contando_vazio == tamanho:
                # Gravando na memoria
                indice_inicio = i - (tamanho - 1)
                indice_termino = i
                flag_gravar = 0
                for j in range(tamanho):
                    memoria[indice_inicio + flag_gravar] = letra
                    flag_gravar += 1
                # PRINTANDO A NOVA MEMÓRIA
                flag_pular_linha = 20
                tamanho_linha = 20
                for i in range(100):
                    if i < (flag_pular_linha - 1) and memoria[i] != letra:
                        print(memoria[i], end=' | ')
                    elif i < (flag_pular_linha - 1) and memoria[i] == letra:
                        print(f'\033[1;31m{memoria[i]}\033[0m', end=' | ')
                        # ~~~~~~~~ Condição mas pulando a linha abaixo
                    elif i == (flag_pular_linha - 1) and memoria[i] != letra:
                        print(memoria[i], end=' |\n', )
                        flag_pular_linha += tamanho_linha
                    else:
                        if i == (flag_pular_linha - 1) and memoria[i] == letra:
                            print(f'\033[1;31m{memoria[i]}\033[0m', end=' |\n')
                            flag_pular_linha += tamanho_linha
                break
            i += 1 # contador para "for'izar" o while no range da memoria apenas
            if i == 99:
                # Mensagem de não achou :(
                print(f'Puts, não encontrei espaço para uma informação tão grande. :(\n'
                      f'Tamanho: {tamanho} | Informação: {letra}')
                break

# ================================================== Segunda Opção
    else:
        if (opcao == 2):
            print(f'Opção Selecionada: 2 - Melhor Escolha\n'
                  f'"Sua informação {letra} de tamanho {tamanho} será armazenada no MENOR espaço disponível que ela caiba inteira."')
            contando_vazio = 0
            melhor_escolha = 0
            indice_melhor_escolha = 0
            achou_lugar = False
            for i in range(100):
                if memoria[i] == ' ':
                    contando_vazio += 1

                # Vendo quantas casas tem além
                if contando_vazio == tamanho:
                    achou_lugar = True
                    espaco_total = i - (i - tamanho)  # Ex: indice 79 - 77 = 2 (tamanho da info)
                    for j in range(i, 100):
                        if memoria[j] == ' ':
                            espaco_total += 1
                        if memoria[j] != ' ':
                            if melhor_escolha == 0:
                                melhor_escolha = espaco_total
                                indice_melhor_escolha = (j)
                                j = 100
                            else:
                                if espaco_total < melhor_escolha:
                                    melhor_escolha = espaco_total
                                    indice_melhor_escolha = (j)
                                    j = 100
                # Zerando se for x
                if memoria[i] != ' ':
                    contando_vazio = 0

            # SE ACHOU LUGAR
            if achou_lugar:
                # Gravando na memoria
                indice_inicio = indice_melhor_escolha - (tamanho)
                flag_gravar = 0
                for k in range(tamanho):
                    memoria[indice_inicio + flag_gravar] = letra
                    flag_gravar += 1
                # PRINTANDO A NOVA MEMÓRIA
                flag_pular_linha = 20
                tamanho_linha = 20
                for i in range(100):
                    if i < (flag_pular_linha - 1) and memoria[i] != letra:
                        print(memoria[i], end=' | ')
                    elif i < (flag_pular_linha - 1) and memoria[i] == letra:
                        print(f'\033[1;31m{memoria[i]}\033[0m', end=' | ')
                        # ~~~~~~~~ Condição mas pulando a linha abaixo
                    elif i == (flag_pular_linha - 1) and memoria[i] != letra:
                        print(memoria[i], end=' |\n', )
                        flag_pular_linha += tamanho_linha
                    else:
                        if i == (flag_pular_linha - 1) and memoria[i] == letra:
                            print(f'\033[1;31m{memoria[i]}\033[0m', end=' |\n')
                            flag_pular_linha += tamanho_linha
            # SE NÃO ACHOU LUGAR
            if not achou_lugar:
                # Mensagem de não achou :(
                print(f'Puts, não encontrei espaço para uma informação tão grande. :(\n'
                      f'Tamanho: {tamanho} | Informação: {letra}')

# ================================================== Terceira Opção
        else:
            if (opcao == 3):
                print(f'Opção Selecionada: 3 - Pior Escolha\n'
                      f'"Sua informação {letra} de tamanho {tamanho} será armazenada no MAIOR espaço disponível."')
                # Deixei os nomes bem declarativos pra ficar fácil retomar mais tarde
                sequencia_atual_espaco_disponivel = 0
                maior_sequencia_espaco_disponivel_registrada = 0
                achou_lugar = False
                for i in range(100):
                    if memoria[i] == ' ':
                        sequencia_atual_espaco_disponivel += 1
                    if memoria[i] != ' ':
                        if maior_sequencia_espaco_disponivel_registrada < sequencia_atual_espaco_disponivel:
                            maior_sequencia_espaco_disponivel_registrada = sequencia_atual_espaco_disponivel
                            indice_maior_sequencia_espaco_disponivel = (i - maior_sequencia_espaco_disponivel_registrada)
                            sequencia_atual_espaco_disponivel = 0
                        sequencia_atual_espaco_disponivel = 0
                    if sequencia_atual_espaco_disponivel == tamanho:
                        achou_lugar = True

                    # Testando se achou
                if achou_lugar:
                    # Gravando na memoria
                    indice_inicio = indice_maior_sequencia_espaco_disponivel
                    flag_gravar = 0
                    for k in range(tamanho):
                        memoria[indice_inicio + flag_gravar] = letra
                        flag_gravar += 1
                    # PRINTANDO A NOVA MEMÓRIA
                    flag_pular_linha = 20
                    tamanho_linha = 20
                    for i in range(100):
                        if i < (flag_pular_linha - 1) and memoria[i] != letra:
                            print(memoria[i], end=' | ')
                        elif i < (flag_pular_linha - 1) and memoria[i] == letra:
                            print(f'\033[1;31m{memoria[i]}\033[0m', end=' | ')
                        # ~~~~~~~~ condição mas pulando a linha abaixo
                        elif i == (flag_pular_linha - 1) and memoria[i] != letra:
                            print(memoria[i], end=' |\n', )
                            flag_pular_linha += tamanho_linha
                        else:
                            if i == (flag_pular_linha - 1) and memoria[i] == letra:
                                print(f'\033[1;31m{memoria[i]}\033[0m', end=' |\n')
                                flag_pular_linha += tamanho_linha
                # SE NÃO ACHOU LUGAR
                if not achou_lugar:
                    # Mensagem de não achou :(
                    print(f'Puts, não encontrei espaço para uma informação tão grande. :(\n'
                          f'Tamanho: {tamanho} | Informação: {letra}')

# ================================================== Você chegou ao fim do código! | Lucas Reinaldo Pacífico | Bacharelado em Engenharia de Software | @lvcaspacifico no github (vou postar só dia 01/07)

