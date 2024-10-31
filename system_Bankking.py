# 1 - Poder depositar valores positivos para conta báncaria.
# 2 - Todos os depósitos dever ser armazenados em uma variável e exibidos na operação de extrato.
# 3 - Sistema deve permitir 3 saques diários, com limite de R$500,00 por saque.
# 4 - Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não é possível sacar o dinheiro por falta de saldo.
# 5 - Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.
# 6 - Essa operação deve listar todos os depósitos e saques realizados na conta.
# 7 - No fim da listagem deve ser exibido o saldo atual da conta.
# 8 - Valores deve ser exibidos utilizando o formato R$ xxx,xx.
# •Exemplo: 1500.45 = R$ 1500.45

extrato = []
account = 0
index = 0

def main_menu():
    print(f'''
    {' Menu Principal '.center(30, '=')}
    Digite [1] - Para depositar.
    Digite [2] - Para sacar.
    Digite [3] - Para ver o extrato bancário.
    ''')

    acesses = int(input('O que deseja acessar? ')) 


    #-------------------------------------------------------
    if acesses == 1:
        global_function_deposity() 

    elif acesses == 2:
        print('Acesso 2')
        # Chamar a função para sacar

    elif acesses == 3:
        print('Acesso 3')
        # Chamar a função para exibir o extrato bancário

    else:
        print("Opção inválida, por favor tente novamente.")
        main_menu()  # Chama novamente o menu principal



#>>>>>>>>>>FUNÇÕES REFERENTE A SEÇÃO DEPOSITAR<<<<<<<<<<<
#>>>>>>>>>>FUNCIONALIDADE DE DEPOSITO DA CONTA<<<<<<<<<<<
def deposity_user():
    while True:
        value = input('>>> Digite o valor que deseja depositar na sua conta: R$ ')
        
        if value == "04":
            main_menu()  # Retorna ao menu principal
            return  # Finaliza a função de depósito

        try:
            # Converte para número decimal
            value = float(value)
            print(f"Depósito de R${value:.2f} realizado com sucesso.")
            extrato.append(value)
            print(extrato)
            # Aqui você adicionaria o valor ao extrato, conta, etc.

        except ValueError:
            print("Valor inválido. Digite um número válido ou '04' para voltar ao menu principal.")
#>>>>>>>>>>VERIFICAÇÃO MAXIMO DE SAQUE<<<<<<<<<<<
def max_sake():
    #Verifica a largura do array e insere na variável number_sakes
    for number_sakes in range(len(extrato)):
        print(number_sakes)
    if number_sakes == 1:
        print('O valor {value} foi inserido em sua conta, você pode fazer mais 2 depositos!')
    elif number_sakes == 2:
        print ('O valor {value} foi inserido em sua conta, você pode fazer mais 1 deposito!')
    else:
        print('Númerp máximo de depositos diários atingidos')
#>>>>>>>>>>FUNÇÃO PRINCIPAL QUE ENGLOBA TODAS AS OUTRAS REFERENTE A DEPOSITO<<<<<<<<<<<
def global_function_deposity():
    print(f'''
    {' Depósito '.center(30, '=')}
    Escreva [04] - Para ir ao menu principal.
    ''')
    deposity_user()
# Função de menu principal para referência
main_menu()


