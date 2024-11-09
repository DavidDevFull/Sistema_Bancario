# 1 - Poder depositar valores positivos para conta báncaria.: (Concluído)
# 2 - Todos os depósitos dever ser armazenados em uma variável e exibidos na operação de extrato.(Concluído)
# 3 - Sistema deve permitir 3 saques diários, com limite de R$500,00 por saque. (Concluído)
# 4 - Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não é possível sacar o dinheiro por falta de saldo.(Concluído)
# 5 - Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.
# 6 - Essa operação deve listar todos os depósitos e saques realizados na conta.
# 7 - No fim da listagem deve ser exibido o saldo atual da conta.
# 8 - Valores deve ser exibidos utilizando o formato R$ xxx,xx.
# •Exemplo: 1500.45 = R$ 1500.45

extract_deposity = []
extract_sakes = []
account_global = 0
#Valor da conta báncaria do usuário
value_of_money_in_species = float(input('>>>Digite o valor que sua conta irá receber para antes de começar:'))

print(f'O valor da sua conta bancária é de:R${value_of_money_in_species:.2f}')

#>>>>>>>>>>FUNÇÃO MENU PRINCIPAL, PRIIMEIRO MENU MOSTRADO<<<<<<<<<<<
def main_menu():
    print(f'''
    {' Menu Principal '.center(50, '=')}
    Digite [1] - Para depositar.
    {'-'.center(50, '-')}
    Digite [2] - Para sacar.
    {'-'.center(50, '-')}
    Digite [3] - Para ver o extrato bancário.
    {' Menu Principal '.center(50, '=')}
    ''')

    acesses = int(input('O que deseja acessar? ')) #    Transforma o valor do input de string para int.

    #-------------------------------------------------------
    
    if acesses == 1:
        global_function_deposity()  # Chamar a função para depositar.

    elif acesses == 2:
        max_sake() # Chamar a função para sacar.

    elif acesses == 3:
        extract_account() # Chamar a função para exibir o extrato bancário.

    else:
        try:
            print("Opção inválida, por favor tente novamente.")
            main_menu()  # Chama novamente o menu principal.
        except:
            print("Opção inválida, por favor tente novamente.")
            main_menu()  # Chama novamente o menu principal.

#>>>>>>>>>>FUNCIONALIDADE DE DEPOSITO DA CONTA<<<<<<<<<<<
def deposity_user():
    global value_of_money_in_species  # Permite modificar a variável global

    while True:
        try:
            # Recebe o valor como string para comparar com "04"
            account_input = input('>>> Digite o valor que deseja depositar na sua conta: R$ ')


            account_global = float(account_input) #Deixa a varivel receber ponto(.) flutuante.

            # Verifica se o usuário deseja voltar ao menu principal
            if account_input == "04":
                main_menu() 
                return  

            #Verifica a se o usuário possui valor em expecie o suficiente para fazer o depósito desejado.
            if account_global > value_of_money_in_species:
                print(f'''
                {' Erro no depósito '.center(50, '=')}
                Não é possível depósitar para sua conta, dinheiro insuficiente!
                {'Erro no depósito '.center(50, '=')}
                ''')
                print(value_of_money_in_species)
                return deposity_user()

            #Verifica se o númeruo é positivo.
            while account_global < 0:
                print(f'''
                 {' Erro no depósito '.center(50, '=')}
                Por favor, digite um valor positivo ou '04' para voltar ao menu principal...
                {' Erro no depósito '.center(50, '=')}
                ''')
                return deposity_user()

            # Realiza o depósito e atualiza o saldo e extrato
            value_of_money_in_species -= account_global #Valor do dinheiro em especie vai ser subtraido pelo valor ataual da conta.
            extract_deposity.append(account_global) #Adicionando um novo valor no array extract.
            print(f'''
                {' Realizado '.center(50, '=')}
                Depósito realizado com sucesso! Saldo atualizado: R${value_of_money_in_species:.2f}
                {' Realizado '.center(50, '=')}
                ''')
            print('Extrato atualizado!')

        # Caso seja digitado letras ou caracteres inválidos                
        except ValueError:

            print(f'''
            {' Erro no depósito '.center(50, '=')}
            Não é possivel inserir letras. Digite um número válido ou '04' para voltar ao menu principal.
            {' Erro no depósito '.center(50, '=')}
            ''')

#>>>>>>>>>>VERIFICAÇÃO MAXIMO DE SAQUE<<<<<<<<<<<
def max_sake():
    while True:
        try:    
            global account_global  # Permite modificar a variável global
            global value_of_money_in_species  # Permite modificar a variável global
            index = 0
            array_mesage_max_deposity = ['Você tem direito a mais 2 depósitos diários',
                                        'Você tem direito a mais 1 depósitos diários',
                                        'Você atingiu o maximo de depósito diários, volte amanhã para fazer mais depósitos'
                                        ]

            account_global = float(account_global) # Valores irá poder ficar com ponto flutuante.
            
            account_global = sum(extract_deposity) # Soma todos os itens do array extract_deposity e faz com que acconunt_global receba os valores somados.

            print(f'Valor atual de dinheiro guardado em sua conta é:{account_global}')
            sake_input = float(input('Digite o valor que deseja sacar da sua conta:'))

            extract_sakes.append(sake_input)

            while sake_input < 0: # Verifica se o númeruo é positivo.
            
                print(f'''
                 {' Erro no depósito '.center(50, '=')}
                Por favor, digite um valor positivo ou '04' para voltar ao menu principal..
                {' Erro no depósito '.center(50, '=')}
                ''')
                return max_sake()

            
            while sake_input > 500: # Se o valor da conta for maior(>) que 500.
                print(f'''
                {' Erro no depósito '.center(50, '=')}
                Por favor digite um valor que seja menor que R$500,00 reais!!!.
                {' Erro no depósito '.center(50, '=')}
                ''')
                return max_sake()

            #index for menor que o raio, minimo da largura do extract_sakes.
            for index in range(min(3 , len(extract_sakes))):
                print(f'''
                {' Procedimento concluido '.center(50, '=')}
                Procedimento de saque foi bem sucedido, dinheiro retirado da sua conta foi no valor de R${sake_input}, o valor que ficará na sua conta é de R${account_global}
                {array_mesage_max_deposity[index]}
                {' Procedimento concluido '.center(50, '=')}
                ''')#Mensagensirá acompanhar o indice e conforme ele é acresentado.

            while len(extract_sakes) > 3:
                extract_sakes.pop()

            print(extract_sakes)
            print(sake_input)
            print(account_global)

        #-------------------------------------------------------
        except ValueError:
            # Caso seja digitado letras ou caracteres inválidos
            print(f'''
            {' Erro no depósito '.center(50, '=')}
            Não é possivel inserir letras. Digite um número válido ou '04' para voltar ao menu principal.
            {' Erro no depósito '.center(50, '=')}
            ''') 
#>>>>>>>>>>EXTRATO DA CONTA E DOS VALORES SACADOS<<<<<<<<<<<
def extract_account():
    print(f'''
    {' Extrato '.center(50, '=')}
    Digite [1] - Para ver o histórico de depositos.
    {'-'.center(50, '-')}
    Digite [2] - Para ver o valor retirado da sua conta.
    {'-'.center(50, '-')}
    Digite [3] - Para voltar para o menu principal.
    {' Extrato '.center(50, '=')}
    ''')

    extract_deposity_sake = int(input('Digite um número e faça a escolha de acordo com os números do menu: '))

    if extract_deposity_sake == 1:
        print('test 1')
        show_extract_deposity()
    elif extract_deposity_sake == 2:
        print('test2')
    elif extract_deposity_sake == 3:
        global_function_deposity()
    else:
        try:
            print(f'''
            {' Erro '.center(50, '=')} 
            >>>Digite um número relacionado ao menu mostrado<<<
            {' Erro '.center(50, '=') }
            ''')
            extract_account()
        except:
            print(f'''
            {' Erro '.center(50, '=')} 
            >>>Digite um número relacionado ao menu mostrado<<<
            {' Erro '.center(50, '=') }
            ''')
            extract_account()

#>>>>>>>>>>EXTRATO DA CONTA<<<<<<<<<<<
def show_extract_deposity():
    total_deosity_of_day = 0
    print(' Depósitos feitos para sua conta! '.center(60, '='))
    for index, value in enumerate(extract_deposity):
        index += 1
        print(f'''
        Depósito de número ({index}) foi: R${value:.2f}
        {'-'.center(50, '-')}
        ''')
    total_deosity_of_day = sum(extract_deposity)
    print(f'''
          {' Total depósitos '.center(50, '=')}
          Valor total depositado hoje foi de: {total_deosity_of_day:.2f}
          {' Total depósitos '.center(50, '=')}
          ''')
    
    back_menu = input('Escerva[OK] para voltar para o menu!').upper()
    if back_menu == 'OK':
        extract_account()
    else:
        show_extract_deposity()
        print(f'''
        {' Erro! '.center(50, '=')}
        Somente letras!
        {' Erro! '.center(50, '=')}
        ''')
#>>>>>>>>>>EXTRATO DOS VALORES SACADOS<<<<<<<<<<<

#>>>>>>>>>>FUNÇÃO PRINCIPAL QUE ENGLOBA TODAS AS OUTRAS REFERENTE A DEPOSITO<<<<<<<<<<<
def global_function_deposity():
    print(f'''
    {' Depósito '.center(50, '=')}
    Escreva [04] - Para ir ao menu principal.
    {' Depósito '.center(50, '=')}
    ''')
    deposity_user()

main_menu()# Função menu principal para referência


