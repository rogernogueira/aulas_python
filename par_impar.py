numero = 2
for i in [5,9,6]:
    numero = int(input("Digite um número inteiro :"))
    if (numero % 2 == 0):
        print("O número "+ str(numero) + " é par")
    else:
        print("O número "+ str(numero) + " é impar")
    print("O valor de i é   -->  ", i)

