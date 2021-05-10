# Programa feito por Ariane Paula Barros (21011817) e João Vitor Gomide Campos (21003360)


def leitura_pedidos (Pedidos):
        Produto = {}

        error = "ok"
    
        cod_pedido = int(input("Digite o código do pedido: "))
        if  cod_pedido != -1:

            quantidade_produtos = int(input("Digite quantos produtos tem nesse pedido: "))
        
            for i in range(quantidade_produtos):
                cod_produto = int(input("\nDigite o código do produto: "))   #verificar se ja foi usado

                while not valida_produto(cod_produto, Tab_Preco):                    
                    print("Produto não encontrado, tente novamente")
                    cod_produto = int(input("\nDigite o código do produto: "))
                    #quantidade_produtos += 1
                    #break
                                  
                quantidade = int(input("Digite a quantidade pedida: "))

                Produto[cod_produto] = quantidade 

            Pedidos[cod_pedido] = [quantidade_produtos, Produto]
        else:
            error = "Pedido inexiste, -1 mano"
           
        #return error
            return -1
        return 0

def imprime_relatorio (Tab_Precos, Pedidos):
        # essa função deverá imprimir o relatório pedido;
    print("\nNo.Pedido  No.Produto  Nome    Quantidade Pedida    Preço Unitário   Valor")

    for pedido_cod, produto_dic in Pedidos.items():     #perguntar se tem como fazer for com and
        #print("{}      {} ".format(pedido_cod, produto_dic[0]))  
        #print(qnt_produtos)
        #print(produto_dic[0]) #qtd produtos
        #print(produto_dic[1])  #código e qtd dele

        cont = 0

        for qtd_cada_prod in (produto_dic[1]).values():
            for myKeys in Tab_Precos.keys():   
                if myKeys == (produto_dic[1]).get(cont):
                    linha =  "      " + str(pedido_cod) + "         " + str((produto_dic[1]).get(cont)) + "              " + str(qtd_cada_prod) + "     "      
                    print(linha)
                cont += 1

        

        #for produto_lista in Tab_Precos.items():   
            #linha += str(produto_dic[0])
            #linha += "      " + str(produto_dic[1])     
            #if produto_lista in produto_dic:
               # print(produto_lista[0])  #codigo do produto
                #print(produto_lista[1])   #nome
                #print(produto_lista[2])  #preco

        

def valida_produto(CodigoProduto, Tab_Precos):
    #– função que retorna True ou False se o código digitado no pedido existe ou não na Tabela de Preços;
    
    if CodigoProduto in Tab_Preco.keys():
        return True
            
    return False

acabou = False
Pedidos = {}
Tab_Preco = {1: ["Barra Diamante Negro 190g", 4.99], 2: ["Barra Lacta Laka 190g", 4.99], 3: ["Caixa de Bis 126g", 4.39], 4: ["Caixa de bombons NESTLE", 12.00],
            5: ["Sorvete 1,5L", 22.99], 6: ["Kit Kat 41,5g", 1.99], 7: ["Trident", 2.99], 8: ["Twix", 2.97], 9: ["Snickers", 2.29],
            10: ["Tubes Morango Azedinho 40g", 2.99], 11: ['Paçoquita 50 unidades', 32.13], 12: ['Sufflair', 4.41]}

while not acabou:

    if leitura_pedidos(Pedidos) == -1:
        acabou = True
        imprime_relatorio(Tab_Preco, Pedidos)
    
    #print(Pedidos)
   

print("Fim do programa \n" + "-------" * 25)