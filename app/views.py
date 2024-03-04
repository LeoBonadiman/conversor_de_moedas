# app/views.py
from flask import Flask, request, jsonify
from .utils import convert_currency

app = Flask(__name__)

@app.route('/converter', methods=['GET'])
def convert_currency_route():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    # Chamando a função de conversão de moeda do módulo utils
    result = convert_currency(from_currency, to_currency, amount)

    return jsonify({'result': result})
