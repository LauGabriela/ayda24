#!/user/bin/env python3
# Declaracion de tupas de nomenclatura
unidades = [
    "",
    "Uno",
    "Dos",
    "Tres",
    "Cuatro",
    "Cinco",
    "Seis",
    "Siete",
    "Ocho",
    "Nueve",
    "Diez",
    "Once",
    "Doce",
    "Trece",
    "Catorce",
    "Quince",
    "Dieciséis",
    "Diecisiete",
    "Dieciocho",
    "Diecinueve",
]
decenas = [
    "",
    "",
    "Veinte",
    "Treinta",
    "Cuarenta",
    "Cincuenta",
    "Sesenta",
    "Setenta",
    "Ochenta",
    "Noventa",
]
decenas_e = [
    "",
    "Veintiuno",
    "Veintidos",
    "Veintitres",
    "Venticuatro",
    "Veinticinco",
    "Ventiseis",
    "Veintisiete",
    "Veintiocho",
    "Veintinueve",
]
centenas = [
    "",
    "Cien",
    "Doscientos",
    "Trescientos",
    "Cuatrocientos",
    "Quinientos",
    "Seiscientos",
    "Setecientos",
    "Ochocientos",
    "Novecientos",
]

# FUNCION QUE PERMITE CONVERTI UN NUMERO EL LETRAS


def Convertir_Numeros(Cantidad):
    if Cantidad < 0:
        return "Solo se permiten numero mayores a 0"
    elif Cantidad == 0:
        return "cero"

    partes = []

    if Cantidad >= 1000000000000:
        Billones = Cantidad // 1000000000000
        partes.append(
            Convertir_Numeros(Billones) + " Billon" + ("es" if Billones > 1 else "")
        )
        Cantidad %= 1000000000000

    if Cantidad >= 1000000000:
        millones = Cantidad // 1000000000
        partes.append(Convertir_Numeros(millones) + " mil")
        Cantidad %= 1000000000

    if Cantidad >= 1000000:
        millones = Cantidad // 1000000
        partes.append(
            Convertir_Numeros(millones) + " millón" + ("es" if millones > 1 else "")
        )
        Cantidad %= 1000000

    if Cantidad >= 1000:
        miles = Cantidad // 1000
        partes.append(Convertir_Numeros(miles) + " mil")
        Cantidad %= 1000

    if Cantidad >= 100:
        Id_Centenas = Cantidad // 100
        letras = ""
        letras = centenas[Id_Centenas]
        if Cantidad % 100 != 0:
            if Id_Centenas == 1:
                letras += "to"
        partes.append(letras)
        Cantidad %= 100

    if Cantidad >= 20:
        Id_Decenas = Cantidad // 10
        if Cantidad > 20 and Cantidad < 30:
            Id_Decenas = Cantidad - 20
            partes.append(decenas_e[Id_Decenas])
            # partes.append("venti")
            # if 0 < Cantidad < 20:
            #    partes.append(unidades[Cantidad])
            Cantidad = 0
        else:
            letras = ""
            letras = decenas[Id_Decenas]
            if Cantidad % 10 != 0:
                if Id_Decenas >= 1:
                    letras += " y"
            partes.append(letras)

        Cantidad %= 10

    if 0 < Cantidad < 20:
        partes.append(unidades[Cantidad])

    return " ".join(partes).strip()


def Validar_Numero():
    while True:
        entrada = input("Ingresa un número: ")
        try:
            numero = int(entrada)  # Puedes usar int() si solo quieres enteros
            return numero
        except ValueError:
            print("No es un número válido. Intenta de nuevo.")


if __name__ == "__main__":
    numero_ingresado = Validar_Numero()
    print(Convertir_Numeros(numero_ingresado))
