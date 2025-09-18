import requests

cnpj    = '43.208.040/0253-92'
url     = 'https://api.opencnpj.org/'


def padronizarCnpj():
   
    cnpjNum = ''.join(filter(str.isdigit, cnpj))
    return cnpjNum
                                                            

def obterDadosEmpresa():

    cnpjNum = padronizarCnpj()
    url_composta = (url + cnpjNum)
    requisicao = requests.get(url_composta)
    requisicao_dic = requisicao.json()
    print("Resposta: ", requisicao_dic)

obterDadosEmpresa()