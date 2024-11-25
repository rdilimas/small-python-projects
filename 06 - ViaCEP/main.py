import requests

def obter_dados_endereco():

    cepEntrada = input("Digite o Cep: ")

    if not cepEntrada.isnumeric():
        print("CEP Não numérico")   
        exit()

    requisicao = requests.get(f"https://viacep.com.br/ws/{cepEntrada}/json/")

    requisicao_dic = requisicao.json()
    print(requisicao_dic)

    #get() para acessar o valor de uma chave, e caso ela não exista no dicionário retornará o valor defaut, no caso abaixo o "false"
    if requisicao_dic.get("erro", "false") == "true":
        print("CEP não encontrado na base")
    else:
        cep        = requisicao_dic["cep"]
        logradouro = requisicao_dic["logradouro"]
        bairro     = requisicao_dic["bairro"]
        localidade = requisicao_dic["localidade"]
        uf         = requisicao_dic["uf"]
        estado     = requisicao_dic["estado"]
        regiao     = requisicao_dic["regiao"]
        ddd        = requisicao_dic["ddd"]
        print(
            "Endereço de Residencia: Rua", logradouro, bairro, localidade,"-", uf  
        )

obter_dados_endereco()