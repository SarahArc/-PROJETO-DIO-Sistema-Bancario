def main():
    menu = '''
    === Menu ===
    
    [1] - Depositar
    [2] - Sacar
    [3] - Exibir extrato
    
    [0] - Sair
    
>> Digite a opção da operação que deseja realizar:  '''

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    LIMITE_DE_SAQUES = 3


    try:
        opcao = int(input(menu))

        while True:
            if opcao == 1:
                valor = float(input("\n>> Digite o valor que deseja depositar: "))

                if valor > 0:
                    saldo += valor
                    extrato += f"    Depósito: R$ {valor:.2f} \n"
                    print(f"\n    Depósito de R$ {valor:.2f} feito com sucesso!")

                    opcao = int(input(menu))

                else:
                    print("\n     VOCÊ NÃO PODE DEPOSITAR VALORES NEGATIVOS.")
                    opcao = int(input(menu))

            elif opcao == 2:
                valor = float(input("\n>> Digite o valor que deseja sacar (você só pode sacar até 500 R$): "))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

                if excedeu_saldo:
                    print("\n     VOCÊ NÃO TEM SALDO SUFICIENTE.")
                    opcao = int(input(menu))

                elif excedeu_limite:
                    print("\n     O VALOR DO SAQUE EXCEDE O LIMITE.")
                    opcao = int(input(menu))


                elif excedeu_saque:
                    print("\n     NÚMERO MAXIMO DE SAQUES ATINGIDOS")
                    opcao = int(input(menu))


                elif valor > 0:
                    saldo -= valor
                    print(f"\n     Saque de {valor:.2f} realizado com sucesso.")
                    extrato += f"    Saque: R$ {valor:.2f} \n"
                    numero_de_saques += 1
                    opcao = int(input(menu))


                else:
                    print("\n O VALOR INFORMADO É INVÁLIDO.")
                    opcao = int(input(menu))


            elif opcao == 3:
                print('=' * 50)
                print("EXTRATO".center(50))
                print("\n     Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\n    Saldo: R$ {saldo:.2f}")
                print('=' * 50, end='\n')

                opcao = int(input(menu))


            elif opcao == 0:
                print('''\n         PROGRAMA ENCERRADO COM SUCESSO.
                    
        Obrigado por utilizar nosso sistema.

                    ''')
                break

            else:
                print("\n   OPERAÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPÇÃO DESEJADA.")
                opcao = int(input(menu))


    except:
        print("\n     ESTE PROGRAMA SÓ ACEITA NÚMEROS, DIGITE NOVAMENTE A OPÇÃO QUE DESEJA.")
        opcao = int(input(menu))


main()