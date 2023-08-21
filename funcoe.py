nome = "python"
def soma_multiplica(valor1,valor2, operacao): 
    
    if operacao =="somar":
        resultado=valor1+valor2
    if operacao =="multiplicar":
        resultado = valor1 * valor2
    return resultado

valor_1 = float(input("Informe o valor 1: "))
valor_2  = float(input("Informe o valor 2: "))
opcao = input("Qual operação: ")
resutado = soma_multiplica(valor_1, valor_2, opcao)
print(resutado)
5
    