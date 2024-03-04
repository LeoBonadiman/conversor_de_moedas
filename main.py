from flask import Flask, request, jsonify
index_html_path = 'frontend/index.html'
obter_taxas_js_path = 'frontend/obter_taxas.js'

app = Flask(__name__)

# Função para realizar a conversão monetária
def realizar_conversao(moeda_origem, moeda_destino, valor):
    return 1000  # Apenas um valor de exemplo

# Rota para realizar a conversão monetária
@app.route('/converter', methods=['GET'])
def converter_moeda():
    # Obter parâmetros da requisição
    moeda_origem = request.args.get('from')
    moeda_destino = request.args.get('to')
    valor = float(request.args.get('amount'))

    resultado = realizar_conversao(moeda_origem, moeda_destino, valor)

    # Retornar o resultado em formato JSON
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)