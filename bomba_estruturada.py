def abastecer_preco(tipo_combustivel, preco):
    abastecimento = 'preco'
    if tipo_combustivel == 'gasolina':
        print(f'Abastecendo com gasolina a R$ {preco:.2f}')
    elif tipo_combustivel == 'alcool':
        print(f'Abastecendo com álcool a R$ {preco:.2f}')
    elif tipo_combustivel == 'diesel':
        print(f'Abastecendo com diesel a R$ {preco:.2f}')
    else:
        print('Combustível inválido')
    return abastecimento
        
def abastecer_litro(tipo_combustivel, litros):
    abastecimento = 'litro'
    if tipo_combustivel == 'gasolina':
        print(f'Abastecendo com {litros:.2f} litros de gasolina')
    elif tipo_combustivel == 'alcool':
        print(f'Abastecendo com {litros:.2f} litros de álcool')
    elif tipo_combustivel == 'diesel':
        print(f'Abastecendo com {litros:.2f} litros de diesel')
    else:
        print('Combustível inválido')
    return abastecimento
        
def valor_combustivel(tipo_combustivel, valor):
    return {tipo_combustivel: valor}

def exibir_dados(valor_combustivel, abastecimento):
    combustivel = list(valor_combustivel.keys())[0]
    preco_litro = valor_combustivel[combustivel]
    
    if abastecimento == 'preco':
        valor_pago = float(input(f'Informe o valor pago por {combustivel}: '))
        litros_abastecidos = valor_pago / preco_litro
        valor_total = valor_pago
    elif abastecimento == 'litro':
        litros_abastecidos = float(input(f'Informe a quantidade de litros de {combustivel} abastecidos: '))
        valor_total = litros_abastecidos * preco_litro
    else:
        print('Modo de abastecimento inválido')
        return
    
    print(f"Tipo de combustível: {combustivel}")
    print(f"Quantidade de litros: {litros_abastecidos:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

def main():
    valor_comb = valor_combustivel('gasolina', 5.80)
    abastecimento = abastecer_preco('gasolina', 20)
    exibir_dados(valor_comb, abastecimento)

if __name__ == "__main__":
    main()
