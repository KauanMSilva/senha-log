produto = input("Digite o nome do produto: ")
estoque = int(input("Digite a quantidade inicial em estoque: "))

controle = input('Deseja registrar uma venda? (s/n): ')

while controle == 's':
    quantidade_vendida = int(input("Digite a quantidade vendida: "))

    if quantidade_vendida > estoque:
        print('Quantidade em estoque insuficiente.')
        print(f'Quantidade em Estoque: {estoque}')
    else:
        estoque -= quantidade_vendida
        print(f"Venda registrada! {quantidade_vendida} unidades vendidas.")

    controle = input('Deseja registrar outra venda? (s/n): ').lower()

print('\n\nRelatório de Estoque:')
print('---------------------')
print(f'Produto: {produto}')
print(f'Quantidade em Estoque: {estoque}')