import requests
import json

# URL da API que fornece os dados dos restaurantes
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

# Realiza uma requisição HTTP GET para obter os dados da API
response = requests.get(url)
print(response)  # Exibe o objeto de resposta para verificar o status da requisição

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Converte os dados recebidos em formato JSON para um objeto Python (lista de dicionários)
    dados_json = response.json()
    
    # Dicionário para organizar os dados por restaurante
    dados_restaurante = {}
    
    # Itera sobre cada item (dicionário) na lista de dados retornada pela API
    for item in dados_json:
        # Obtém o nome do restaurante (chave "Company")
        nome_do_restaurante = item['Company']
        
        # Se o restaurante ainda não está no dicionário, cria uma lista para ele
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        # Adiciona os itens do restaurante à lista no dicionário
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],         
            "price": item['price'],       
            "description": item['description'] 
        })

else:
    # Caso a requisição falhe, exibe o código de erro HTTP
    print(f'O erro foi {response.status_code}')

# Itera sobre o dicionário para salvar os dados de cada restaurante em um arquivo JSON separado
for nome_do_restaurante, dados in dados_restaurante.items():
    # Define o nome do arquivo baseado no nome do restaurante
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    
    # Abre o arquivo no modo de escrita ('w') com codificação UTF-8
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
        # Salva os dados do restaurante no arquivo JSON com indentação para facilitar a leitura
        json.dump(dados, arquivo_restaurante, indent=4)
