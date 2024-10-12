def add(a, b):
    return a + b


x = eval(input("inserta numero  a"))  # nosec B307:blacklist
y = eval(input("inserta numero  b"))  # nosec B307:blacklist
txt = "Suma {:.2f}"
print(txt.format(add(x, y)))
