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




def main_menu():
    print(f'''
    {' Menu Principal '.center(50, '=')}
    Digite [1] - Para depositar 🤲🏻💵🏦.
    Digite [2] - Para sacar 🖐🏻💵🏦.
    Digite [3] - Para ver o extrato bancário📓.
    {' Menu Principal '.center(50, '=')}
    ''')

    acesses = int(input('O que deseja acessar? ')) 


    #-------------------------------------------------------
        #Chamar função para depositar.
    if acesses == 1:
        global_function_deposity() 

    elif acesses == 2:
        max_sake()
        # Chamar a função para sacar.

    elif acesses == 3:
        print('Acesso 3')
        # Chamar a função para exibir o extrato bancário.

    else:
        print("Opção inválida, por favor tente novamente.")
        main_menu()  # Chama novamente o menu principal.

#>>>>>>>>>>FUNÇÕES REFERENTE A SEÇÃO DEPOSITAR<<<<<<<<<<<
#>>>>>>>>>>FUNCIONALIDADE DE DEPOSITO DA CONTA<<<<<<<<<<<
def deposity_user():
    global value_of_money_in_species  # Permite modificar a variável global

    while True:
        try:
            # Recebe o valor como string para comparar com "04"
            account_input = input('>>> Digite o valor que deseja depositar na sua conta: R$ ')


            account_global = float(account_input)

            # Verifica se o usuário deseja voltar ao menu principal
            if account_input == "04":
                main_menu() 
                return  
            
            #Verifica se o númeruo é positivo.
            while account_global < 0:
                print(f'''
                 {' Erro no depósito '.center(50, '=')}
                Por favor, digite um valor positivo ou '04' para voltar ao menu principal..
                ''')
                break

            #Verifica a se o usuário possui valor em expecie o suficiente para fazer o depósito desejado.
            if account_global > value_of_money_in_species:
                print(f'''
                {' Erro no depósito '.center(50, '=')}
                Não é possível depósitar para sua conta, dinheiro insuficiente!
                {'Erro no depósito '.center(50, '=')}
                ''')
                print(value_of_money_in_species)
                return deposity_user()

            # Realiza o depósito e atualiza o saldo e extrato
            
            value_of_money_in_species -= account_global
            extract_deposity.append(account_global)
            print(f'''
                {' Realizado '.center(50, '=')}
                Depósito realizado com sucesso! Saldo atualizado: R${value_of_money_in_species:.2f}
                {' Realizado '.center(50, '=')}
                ''')
            print("Extrato atualizado:", extract_deposity)
                
        except ValueError:
            # Caso seja digitado letras ou caracteres inválidos
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

            account_global = float(account_global)
            
            account_global = sum(extract_deposity)

            print(f'Valor atual de dinheiro guardado em sua conta é:{account_global}' )
            sake_input = float(input('Digite o valor que deseja sacar da sua conta:'))

            #Verifica se o númeruo é positivo.
            while sake_input < 0:
                print(f'''
                 {' Erro no depósito '.center(50, '=')}
                Por favor, digite um valor positivo ou '04' para voltar ao menu principal..
                ''')
                break

            # Se o valor da conta for maior(>) que 500.
            while sake_input >= 500:
                print(f'''
                {' Erro no depósito '.center(50, '=')}
                Por favor digite um valor que seja menor que R$500,00 reais!!!.
                {' Erro no depósito '.center(50, '=')}
                ''')
                break
            #Valor da conta menos o valor digitado que deseja ser retirado.
            account_global - sake_input
            #value_of_money_in_species += sake_input
            extract_sakes.append(sake_input)



            for index in range(min(3 , len(extract_sakes))):
                print(f'''
                {' Procedimento concluido '.center(50, '=')}
                Procedimento de saque foi bem sucedido, dinheiro retirado da sua conta foi no valor de R${sake_input}, o valor que ficará na sua conta é de R${account_global}
                {array_mesage_max_deposity[index]}
                {' Procedimento concluido '.center(50, '=')}
                ''')
            while len(extract_sakes) > 3:
                extract_sakes.pop()
            print(extract_sakes)
            print(account_global)

 

        except ValueError:
            # Caso seja digitado letras ou caracteres inválidos
            print(f'''
            {' Erro no depósito '.center(50, '=')}
            Não é possivel inserir letras. Digite um número válido ou '04' para voltar ao menu principal.
            {' Erro no depósito '.center(50, '=')}
            ''') 



#>>>>>>>>>>FUNÇÃO PRINCIPAL QUE ENGLOBA TODAS AS OUTRAS REFERENTE A DEPOSITO<<<<<<<<<<<
def global_function_deposity():
    print(f'''
    {' Depósito '.center(50, '=')}
    Escreva [04] - Para ir ao menu principal.
    {' Depósito '.center(50, '=')}
    ''')
    deposity_user()
# Função de menu principal para referência
main_menu()


