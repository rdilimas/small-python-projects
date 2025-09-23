## Pequenos projetos em Python (Estudos)

### Projeto
1. Obtenção de dados de Empresa
    1. [API OpenCNPJ](https://opencnpj.org/)
        1. OpenCNPJ é uma API pública e gratuita para consultar dados cadastrais de empresas brasileiras por CNPJ. Informe um CNPJ válido e receba uma resposta JSON simples, pronta para uso em aplicativos, integrações e automações.
        
    2. Como remover caracteres especiais e deixar apenas números em uma string

       | Parte do código             | O que faz                                                |
       | --------------------------- | ---------------------------------------------------------------- |
       | `cnpj`                      | String original contendo letras, símbolos e números.|
       | `str.isdigit`               | Função que retorna `True` se o caractere for um número (`0` a `9`). |
       | `filter(str.isdigit, cnpj)` | Filtra todos os caracteres da string, mantendo **apenas os dígitos**. |
       | `''.join(...)`              | Junta os dígitos filtrados em uma nova string, sem espaços ou separadores. |
       | `cnpjNum`                   | Variável que recebe o resultado final, como `"12345678000195"`.


       💡 `Vantagens dessa abordagem`
        - ✅ Simples e legível
        - ✅ Rápida e eficiente
        - ✅ Não requer bibliotecas externas
        - ✅ Fácil de aplicar em listas ou colunas de DataFrame  
          

        🧪 `Aplicações comuns`
        - ✅ Limpeza de dados (CPF, CNPJ, telefones)
        - ✅ Preparação para validação ou envio para APIs
        - ✅ Normalização de campos em bancos de dados

