import requests
from phonenumbers import format_number, PhoneNumberFormat, parse
import utils

#cnpj    = '06.057.223/0001-71'
#cnpj    = '75.315.333/0001-09'
cnpj    = '43.208.040/0253-92'
url     = 'https://api.opencnpj.org/'

def main():
    dados_empresa = obterDadosEmpresa()
    processarDadosEmpresa(dados_empresa)

def padronizarCnpj():
    
   
    cnpjNum = ''.join(filter(str.isdigit, cnpj))
    return cnpjNum
                                                            

def obterDadosEmpresa():

    cnpjNum = padronizarCnpj()
    url_composta = (url + cnpjNum)
    requisicao = requests.get(url_composta)
    requisicao_dic = requisicao.json()

    return requisicao_dic

def imprimirDadosBasicos(razao_social, nome_fantasia, situacao_cadastral,
                         data_situacao_cadastral, matriz_filial, data_inicio_atividade,
                         cnae_principal,natureza_juridica):
    
    print(      "CNPJ......................:",cnpj, 
              "\nRazão Social..............:",razao_social, 
              "\nNome Fantasia.............:",nome_fantasia , 
              "\nSituação Cadastral........:",situacao_cadastral,
              "\nData da Situação..........:",utils.formatarData(data_situacao_cadastral, 4, 2), 
              "\nMatriz/Filial.............:",matriz_filial, 
              "\nData Inicio Atividade.....:",utils.formatarData(data_inicio_atividade, 4, 2),
              "\nCNAE Principal............:",cnae_principal,
              "\nNatureza Juridica.........:",natureza_juridica)
    
def imprimirEndereco(logradouro, numero, complemento,
                     bairro, cep, uf, municipio):
    
    print(f"\nEndereço..................: {logradouro}, Nº {numero} {bairro} CEP: {cep} - {municipio}/{uf}")
                                              
def montarListaCNAES(cnaes):

        for i, cnae in enumerate(cnaes, start=2):
            print(f"  - CNAE {i:02}...............: {cnae}")

def montarListaTelefones(telefones,email):

    print("Email.....................:", email)
    
    qtd_telefones = len(telefones)
    contador = 0

    while contador < qtd_telefones:
        ddi      = +55
        ddd      = telefones[contador].get("ddd", "ddd não encontrado")
        telefone = telefones[contador].get("numero", "Numero não encontrado")
        is_fax   = telefones[contador].get("is_fax", "Fax não encontrado")
        
        if is_fax:
           is_fax = "Sim"
        else:
           is_fax = "Não"

        numero_bruto = str(ddi) + str(ddd) + str(telefone)
        numero = parse(numero_bruto, "BR")
        numero_completo = format_number(numero, PhoneNumberFormat.NATIONAL)

        i = contador+1
        print(f"Contato {i:02}................: {numero_completo} Fax: {is_fax}")
        contador += 1         

# obter quadro de socios
#  
def montarListaSocios(socios):  

   

    qtd_socios = len(socios)
    contador = 0
    str_socios = "SÓCIO-"

    if qtd_socios > 1:
       str_socios = "SÓCIOS"
  
    print(f"\n----------{str_socios}----------:") 

    while contador < qtd_socios:

        nome_socio              = socios[contador].get("nome_socio", "Nome não encontrado")
        cnpj_cpf_socio          = socios[contador].get("cnpj_cpf_socio", "CNPJ/CPF não encontrado")
        qualificacao_socio      = socios[contador].get("qualificacao_socio", "Qualificação não encontrada")
        data_entrada_sociedade  = socios[contador].get("data_entrada_sociedade", "Data não encontrado")
        identificador_socio     = socios[contador].get("identificador_socio", "Tipo Pessoa não encontrado")
        faixa_etaria            = socios[contador].get("faixa_etaria", "Faixa Etária não encontrado")        
        
        print(  "\n"
                "   Nome...................:",nome_socio , 
              "\n   CNPJ/CPF...............:",cnpj_cpf_socio , 
              "\n   Qualificação...........:",qualificacao_socio,
              "\n   Data de Entrada........:",utils.formatarData(data_entrada_sociedade, 4, 2), 
              "\n   Tipo de Pessoa.........:",identificador_socio, 
              "\n   Faixa Etária...........:",faixa_etaria)
        contador += 1   

def processarDadosEmpresa(dic_empresa):
     
#   bloco de dados "básicos"    
    razao_social            = dic_empresa.get("razao_social")
    nome_fantasia           = dic_empresa.get("nome_fantasia")
    situacao_cadastral      = dic_empresa.get("situacao_cadastral", "Situação Não encontrada")
    data_situacao_cadastral = dic_empresa.get("data_situacao_cadastral")
    matriz_filial           = dic_empresa.get("matriz_filial")
    data_inicio_atividade   = dic_empresa.get("data_inicio_atividade")
    cnae_principal          = dic_empresa.get("cnae_principal")
    natureza_juridica       = dic_empresa.get("natureza_juridica")
    
    imprimirDadosBasicos(razao_social, nome_fantasia, situacao_cadastral,
                         data_situacao_cadastral, matriz_filial, data_inicio_atividade,
                         cnae_principal,natureza_juridica)
    cnaes                   = dic_empresa.get("cnaes_secundarios")
    montarListaCNAES(cnaes)

#   bloco de endereço
    logradouro  = dic_empresa.get("logradouro")
    numero      = dic_empresa.get("numero")
    complemento = dic_empresa.get("complemento")
    bairro      = dic_empresa.get("bairro")
    cep         = dic_empresa.get("cep")
    uf          = dic_empresa.get("uf")
    municipio   = dic_empresa.get("municipio")
    email       = dic_empresa.get("email")

    imprimirEndereco(logradouro, numero, complemento,
                     bairro, cep, uf, municipio)

    telefones   = dic_empresa.get("telefones")
    montarListaTelefones(telefones, email)  
    
    socios      = dic_empresa.get("QSA")
    montarListaSocios(socios)
    
main()