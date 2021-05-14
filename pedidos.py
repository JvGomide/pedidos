# Programa feito por Ariane Paula Barros (21011817) e João Vitor Gomide Campos (21003360)


def leitura_pedidos (Pedidos):
        Produto = {}

        try:
            
            cod_pedido = int(input("\nDigite o código do pedido: "))

            while cod_pedido < -1:
                print('Código de pedido inválido, tente novamente')
                cod_pedido = int(input("\nDigite o código do pedido: "))
            
            if  cod_pedido != -1 and cod_pedido > 0:
                
                quantidade_produtos = int(input("Digite quantos produtos tem nesse pedido: "))
                while quantidade_produtos < 1:
                    print("Quantidade inválida, tente novamente")
                    quantidade_produtos = int(input("Digite quantos produtos tem nesse pedido: "))
            
                for i in range(quantidade_produtos):
                    cod_produto = int(input("\nDigite o código do produto: "))

                    while not valida_produto(cod_produto, Tab_Preco) or cod_produto < 0:                    
                        print("Produto não encontrado, tente novamente")
                        cod_produto = int(input("\nDigite o código do produto: "))
              
                    quantidade = int(input("Digite a quantidade pedida: "))
                    while quantidade < 1:
                        print("Quantidade inválida, tente novamente")
                        quantidade = int(input("Digite a quantidade pedida: "))

                    Produto[cod_produto] = quantidade 

                Pedidos[cod_pedido] = [quantidade_produtos, Produto]
            else:           
                return -1
            
            return Pedidos
        except:
            print("Erro, digite apenas valores válidos!")

def imprime_relatorio (Tab_Precos, Pedidos):
    print(f'{"No.Pedido": <3}      {"No.Produto": <4}     {"Nome": <24}    {"Quantidade Pedida": <3}    {"Preço Unitário": <6}    {"Valor": <8}')

    for pedido_cod, produto_dic in Pedidos.items():  

        listinhaCod = list((produto_dic[1]).keys())
        listinhaQtd = list((produto_dic[1]).values())
        
        cont = 1
        for myKeys in Tab_Precos.keys():
            if len(listinhaCod) == 0:
                break
            else:
                if myKeys == listinhaCod[0]:         
                    print(f'\n{str(pedido_cod).zfill(4): ^8}  {str(listinhaCod[0]).zfill(3): ^19} {Tab_Precos[cont][0]: <23}  {str(listinhaQtd[0]): ^23} {str(Tab_Precos[cont][1]): ^14}  {str(listinhaQtd[0] * Tab_Precos[cont][1]): ^10}')
                    listinhaCod.pop(0)
                    listinhaQtd.pop(0)
            cont += 1
        

def valida_produto(CodigoProduto, Tab_Preco):
    if CodigoProduto in Tab_Preco.keys():
        return True
            
    return False


Pedidos = {}

while True:
    Tab_Preco = {1: ["Barra Diamante Negro 190g", 4.99], 2: ["Barra Lacta Laka 190g", 4.99], 3: ["Caixa de Bis 126g", 4.39], 4: ["Caixa de bombons NESTLE", 12.00],
            5: ["Sorvete 1,5L", 22.99], 6: ["Kit Kat 41,5g", 1.99], 7: ["Trident", 2.99], 8: ["Twix", 2.97], 9: ["Snickers", 2.29],
            10: ["Tubes Morango Azedinho 40g", 2.99], 11: ['Paçoquita 50 unidades', 32.13], 12: ['Sufflair', 4.41]}

    retorno = leitura_pedidos(Pedidos)
    if retorno == -1:
        imprime_relatorio(Tab_Preco, Pedidos)
        break
    

print("Fim do programa \n" + "-------" * 25)