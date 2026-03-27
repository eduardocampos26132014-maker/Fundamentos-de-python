valor = float(input("Insira um valor"))

if valor < 85.528:
    tax = valor * 0.18 - 556.02
    print("Seu imposto calculado é", tax)
elif valor > 85.528:
    tax = valor * 0.32 + 14.839
    print("A Taxa é", tax) 
else:
    tax = round(tax, 0)
    print("A taxa é:", tax, "thalers") 
 