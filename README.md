# Simulador de Bomba de Combustível ⛽️🚗

Este é um simulador de uma bomba de combustível desenvolvido como parte de um exercício da disciplina de Estrutura de Dados, na faculdade. Ele permite simular o funcionamento de uma bomba de combustível, oferecendo funcionalidades básicas de abastecimento de veículos.

### Abstração da Bomba de Combustível 🛢️

A bomba de combustível é uma máquina utilizada para abastecer veículos com diferentes tipos de combustível, como gasolina, etanol e diesel. Suas principais características incluem:

- **Tipo de Combustível:** A bomba oferece diferentes tipos de combustível para abastecimento, como gasolina comum, gasolina aditivada, etanol e diesel.

- **Valor do Litro:** Cada tipo de combustível possui um valor por litro, determinado pelas condições de mercado.

- **Capacidade de Abastecimento:** A bomba é capaz de abastecer o veículo com a quantidade desejada de combustível, até atingir o limite do tanque do veículo.

### Tipo Abstrato de Dados e Operações 📝

Com base na abstração da bomba de combustível, podemos definir o seguinte Tipo Abstrato de Dados (TAD) e suas operações:

- **TAD BombaDeCombustivel:**
  - `selecionar_combustivel(tipo_combustivel)`: Seleciona o tipo de combustível desejado para abastecimento.
  - `abastecer(valor_litro, quantidade_litros)`: Abastece o veículo com a quantidade desejada de combustível, calculando o valor total do abastecimento.
  - `exibir_valor_total()`: Exibe o valor total do abastecimento realizado.
  
### Implementação Estruturada 🛠️

Para implementar o programa estruturado que simula o funcionamento da bomba de combustível, criamos funções para cada operação definida no TAD. O programa principal realiza os testes dessas operações.

### Implementação Orientada a Objetos 🎨

Na implementação orientada a objetos, a bomba de combustível é representada como um objeto da classe `BombaDeCombustivel`. Esta classe possui métodos que correspondem às operações definidas no TAD. Utilizamos o mesmo programa principal da implementação estruturada para testar a bomba de combustível como um objeto.
