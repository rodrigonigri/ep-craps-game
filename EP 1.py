from random import randint
Fichas_iniciais=1000
print("Fichas iniciais: {0}".format(Fichas_iniciais))
a = True
b = True
print('Faça sua aposta e decida quanto você quer apostar. As possíveis apostas são: Pass_line, Field, Any_Craps e Twelve')
aposta = input("Escolha uma aposta dentre as 4 acima: ")
quantidade=int(input("Quanto você quer apostar: "))
while b:
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    if aposta == "Pass_line":
        print('Você está na fase Come out')
        if dado_1+dado_2 == 7 or dado_1+dado_2 == 11:
            print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
            print("PARABENS, VOCÊ GANHOU")
            Fichas_iniciais = Fichas_iniciais+quantidade
            b=False
            print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
        elif dado_1+dado_2 == 2 or dado_1+dado_2 == 3 or dado_1+dado_2 == 12:
            print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
            Fichas_iniciais-= quantidade
            print("NÃO FOI DESSA VEZ")
            print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
            b=False
        else:
            print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
            print('Você foi para a FASE POINT')
            point=dado_1+dado_2
            print("O seu Point é {0}".format(point))
            b=False
            while a:
                dado_3=randint(1,6)
                dado_4=randint(1,6)
                print("Os dados foram {0} e {1} somando {2}".format(dado_3,dado_4,dado_3+dado_4))
                if dado_3+dado_4 == point:
                    print('PARABÉNS, VOCÊ GANHOU')
                    Fichas_iniciais=Fichas_iniciais+quantidade
                    a=False
                    print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
                elif dado_3+dado_4 == 7:
                    print("NÃO FOI DESSA VEZ")
                    Fichas_iniciais-=quantidade
                    a=False
                    print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
                else:
                    a=True
