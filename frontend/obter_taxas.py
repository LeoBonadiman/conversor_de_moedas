import requests

# Função para obter as taxas de câmbio do Open Exchange Rates
def obter_taxas_de_cambio(api_key):
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        if 'rates' in data:
            return data['rates']
        else:
            print("Erro ao obter as taxas de câmbio.")
            return None
    except Exception as e:
        print(f"Erro ao fazer solicitação à API: {e}")
        return None

# Testando a função
api_key = '29a4986c49c140c193b7da5ec534006c' 
taxas = obter_taxas_de_cambio(api_key)
if taxas:
    print(taxas)