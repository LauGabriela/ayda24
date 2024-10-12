# Función para convertir números a texto en inglés
def number_to_text(num):
    if num < 0:
        return "minus " + number_to_text(-num)

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 10:
        return units[num]
    elif 10 <= num < 20:
        return teens[num - 10]
    elif 20 <= num < 100:
        d = num // 10
        u = num % 10
        return tens[d] + ('' if u == 0 else '-' + units[u])
    elif 100 <= num < 1000:
        c = num // 100
        d = num % 100
        return units[c] + ' hundred' + ('' if d == 0 else ' and ' + number_to_text(d))
    elif 1000 <= num < 1_000_000:
        m = num // 1000
        return number_to_text(m) + ' thousand' + ('' if num % 1000 == 0 else ' ' + number_to_text(num % 1000))
    elif 1_000_000 <= num < 1_000_000_000:
        m = num // 1_000_000
        return number_to_text(m) + ' million' + ('' if num % 1_000_000 == 0 else ' ' + number_to_text(num % 1_000_000))
    elif 1_000_000_000 <= num < 1_000_000_000_000:
        b = num // 1_000_000_000
        return number_to_text(b) + ' billion' + ('' if num % 1_000_000_000 == 0 else ' ' + number_to_text(num % 1_000_000_000))
    elif 1_000_000_000_000 <= num < 1_000_000_000_000_000:
        trillion = num // 1_000_000_000_000
        return number_to_text(trillion) + ' trillion' + ('' if num % 1_000_000_000_000 == 0 else ' ' + number_to_text(num % 1_000_000_000_000))

    return str(num)  # Para números mayores a trillones

# Solicitar un número al usuario
number = int(input("Enter a number (up to trillions): "))

# Convertir el número a texto
text = number_to_text(number)

# Mostrar el resultado
print(f"The number {number} in words is: {text}")
