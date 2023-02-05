#Introduzir o numero
numero = int(input("Coloque o numero : "))

#iniciazar o intervalo de valores 1 2 3 por causa do cem, duzentos e trezentos
intervalo_123 = 0

#Funcao para converter o numero em seu equivalente em palavra
def converter_para_letra(numero):
    #Valores de 0 para 19
    unidades = ["Zero", "Um", "Dois", "Très", "Quatro", "Cinco",
                "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
                "Treze", "Catorze", "Quinze", "Dezesseis","Dezessetee",
                "Dezoito", "Dezenove"]

    #Valores de 20 para 90
    Dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta",
               "Setenta", "Oitenta", "Noventa"]
    if numero < 20:
        return unidades[numero]

    elif numero < 100:
        return Dezenas[numero // 10] + (' ' if numero % 10 == 0 else ' ' + unidades[numero % 10])

    elif numero < 1000:
        intervalo_123 = numero // 100

        if intervalo_123 in [1,2,3]:
            
            if (intervalo_123 == 1):
                return ('Cem' if numero % 100 == 0 else 'Cento ' + converter_para_letra(numero % 100))

            elif (intervalo_123 == 2):
               return "Duzentos" + (' ' if numero % 100 == 0 else ' ' + converter_para_letra(numero % 100))

            elif (intervalo_123 == 3):
                return "Trezentos" + (' ' if numero % 100 == 0 else ' ' + converter_para_letra(numero % 100))
            
        else:
            return unidades[numero // 100] + " Centos" + (' ' if numero % 100 == 0 else ' ' +
                                                         converter_para_letra(numero % 100))
print(converter_para_letra(numero))
