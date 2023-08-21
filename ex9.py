numero_a_ser_advinhado = 20
while True:
    palpite = int(input("Digite seu palpite :"))
    if numero_a_ser_advinhado == palpite:
        print("Parabens vc acertou")
        break
    if palpite > numero_a_ser_advinhado:
        print("Tente novamente. Dica : Numero é menor")
    else:
        print("Tente novamente. Dica : Numero é maior")

    
    