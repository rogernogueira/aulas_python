idade = int(input("digite sua idade :"))
peso = int(input("digite seu peso :"))
sono_noite_anterior = int(input("quanta horas vc durmio na noite anterior? : "))

if (idade > 16) and(idade < 69) and(peso > 50) and (sono_noite_anterior >= 6):
        print("vc pode doar sangue")
else : 
        print("Vc não pode doar sangue")                        