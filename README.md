# Conversor de Moedas

Um aplicativo simples para converter entre diferentes moedas usando taxas de câmbio atuais.

## Como usar

1. Clone o repositório:
git clone https://github.com/seu-usuario/conversor-de-moedas.git
cd conversor-de-moedas

2. Instale as dependências:
pip install -r requirements.txt

3. Inicie a aplicação:
python main.py

4. Acesse a aplicação em http://localhost:5000 no seu navegador.

## Como funciona

A aplicação usa uma API para obter as taxas de câmbio atuais entre diferentes moedas. Você pode converter entre moedas especificando a moeda de origem, a moeda de destino e o valor a ser convertido na URL da API.

Por exemplo, para converter 100 USD para BRL, acesse:
http://localhost:5000/converter?from=USD&to=BRL&amount=100

Isso retornará o valor convertido em formato JSON.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
