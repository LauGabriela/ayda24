def convertir_a_letras(n):
    unidades = (
        "",
        "uno",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
        "diez",
        "once",
        "doce",
        "trece",
        "catorce",
        "quince",
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    )
    decenas = (
        "",
        "",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    )
    centenas = (
        "",
        "cien",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    )

    def convertir_menor_1000(n):
        if n == 0:
            return ""
        elif n < 20:
            return unidades[n]
        elif n < 100:
            if n % 10 == 0:
                return decenas[n // 10]
            else:
                return decenas[n // 10] + " y " + unidades[n % 10]
        else:
            if n % 100 == 0:
                return centenas[n // 100]
            else:
                return centenas[n // 100] + " " + convertir_menor_1000(n % 100)

    def convertir_grande(n):
        if n == 0:
            return "cero"
        if n == 1_000_000_000:
            return "un billón"

        partes = []
        miles = ["", "mil", "millón", "mil millones"]
        i = 0

        while n > 0:
            parte = n % 1000
            if parte != 0:
                if i == 1 and parte == 1:
                    partes.append("mil")
                elif i > 1 and parte == 1:
                    partes.append("un " + miles[i])
                else:
                    partes.append(convertir_menor_1000(parte) + " " + miles[i])
            n //= 1000
            i += 1

        return " ".join(reversed(partes)).strip()

    return convertir_grande(n)


# Ejemplo de uso:
numero = 123454
print(convertir_a_letras(numero))
