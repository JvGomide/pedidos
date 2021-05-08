# Programa feito por Ariane Barros e João Vitor: 21003360

end = False

while not end:
    Pedido = {}
    
    cod_pedido = int(input("Digite o código do pedido: "))

    quantidade_pedida = int(input("Digite quantos produtos tem nesse pedido: "))
    for i in range(quantidade_pedida):
        num_produto = int(input("Digite o número do produto: "))
        quantidade = int(input("Digite a quantidade pedida: "))

    Pedido[cod_pedido] = [quantidade_pedida, num_produto, quantidade]

    Pedido

    break
print("Fim do programa \n" + "-------" * 25)