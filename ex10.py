total = 0
imposto  = 0.1

while True:
    valor_item = input("Digite o valor do item ou s para sair")
    if valor_item=='s':
        break
    total =total+float(valor_item)

total = total*imposto + total


print("o valor total é : ", total)