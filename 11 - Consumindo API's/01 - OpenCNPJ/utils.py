from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def formatarData(dataEntrada, codFormatEntrada, codFormatSaida):

    
    match codFormatEntrada:
        case 1:                                   # Padrão brasileiro
            codFormatSaida = "%d/%m/%Y"                # 13/04/2018

        case 2:                                   # Padrão americano
            codFormatSaida = "%m/%d/%Y"                # 04/13/2018

        case 3:                                   # Nome do mês por extenso
            codFormatSaida = "%d de %B de %Y"          # 13 de April de 2018

        case 4:                                   # Dia da semana
            codFormatSaida = "%A, %d/%m/%Y"            # Friday, 13/04/2018

        case 5:                                   # Data compacta, sem formatação
            codFormatSaida = "%Y%m%d"                  # 20180413  

        case 6:                                   # Dia do ano
            codFormatSaida = "%j"                      # 103 (13 de abril é o 103º dia do ano)    

        case 7:                                   # Semana do ano
            codFormatSaida = "Semana %U"               # Semana 15    


    #Formatos previstos na entrada    
    if codFormatEntrada == 1:
        codFormatEntrada = "%d-%m-%Y"
    else:
        codFormatEntrada = "%Y-%m-%d"

    data = datetime.strptime(dataEntrada, codFormatEntrada)

    data_formatada = datetime.strftime(data, codFormatSaida)
    return data_formatada

'''print(formatarData("13-04-2018", 1, 1))
print(formatarData("2018-04-13", 2, 2))
print(formatarData("2018-04-13", 3, 2))
print(formatarData("2018-04-13", 4, 2))
print(formatarData("2018-04-13", 5, 2))
print(formatarData("2018-04-13", 6, 2))
print(formatarData("2018-04-13", 7, 2))'''