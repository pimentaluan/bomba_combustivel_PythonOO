class BombaCombustivel:
    def __init__(self):
        self.valor_combustivel = {}

    def abastecer_preco(self, tipo_combustivel, preco):
        if tipo_combustivel not in self.valor_combustivel:
            print("Tipo de combustível não cadastrado.")
            return

        litros_abastecidos = preco / self.valor_combustivel[tipo_combustivel]
        self.ultimo_abastecimento = (tipo_combustivel, preco, litros_abastecidos, 'preco')
        return litros_abastecidos

    def abastecer_litro(self, tipo_combustivel, litros):
        if tipo_combustivel not in self.valor_combustivel:
            print("Tipo de combustível não cadastrado.")
            return

        valor_pago = litros * self.valor_combustivel[tipo_combustivel]
        self.ultimo_abastecimento = (tipo_combustivel, valor_pago, litros, 'litro')
        return valor_pago

    def exibir_dados(self):
        if not hasattr(self, 'ultimo_abastecimento'):
            print("Nenhum abastecimento foi realizado ainda.")
            return

        tipo_combustivel, valor_pago, quantidade, modo_abastecimento = self.ultimo_abastecimento
        if modo_abastecimento == 'preco':
            print(f"Tipo de combustível: {tipo_combustivel}")
            print(f"Quantidade de litros: {quantidade:.2f}")
            print(f"Valor total: R$ {valor_pago:.2f}")
        elif modo_abastecimento == 'litro':
            print(f"Tipo de combustível: {tipo_combustivel}")
            print(f"Quantidade de litros: {quantidade:.2f}")
            print(f"Valor total: R$ {valor_pago:.2f}")
        else:
            print('Modo de abastecimento inválido')

    def combustivel_valor(self, tipo_combustivel, valor):
        self.valor_combustivel[tipo_combustivel] = valor


def main():
    bomba = BombaCombustivel()
    bomba.combustivel_valor('gasolina', 5.80)
    bomba.abastecer_preco('gasolina', 20)
    bomba.exibir_dados()

if __name__ == "__main__":
    main()
