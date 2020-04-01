from random import randint
Fichas_iniciais=1000
a = True
b = True
print('Faça sua aposta e decida quanto você quer apostar. As possíveis apostas são: Pass_line, Field, Any_craps e Twelve')
while b and Fichas_iniciais>0:
    pergunta=input('Você quer continuar?(sim/não): ')
    if pergunta=="não":
        b = False
    else:
        aposta = input("Escolha uma aposta dentre as 4(Pass_line, Field, Any_craps e Twelve): ")
        print("Fichas iniciais: {0}".format(Fichas_iniciais))
        quantidade=int(input("Quanto você quer apostar???(OBS:. Para jogar honestamente, coloque um valor menor ou igual a sua quantidade atual): "))
        dado_1 = randint(1,6)
        dado_2 = randint(1,6)
        if aposta == "Pass_line":
            print('Você está na fase Come out')
            if dado_1+dado_2 == 7 or dado_1+dado_2 == 11:
                print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABENS, VOCÊ GANHOU")
                Fichas_iniciais = Fichas_iniciais+quantidade
                print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
            elif dado_1+dado_2 == 2 or dado_1+dado_2 == 3 or dado_1+dado_2 == 12:
                print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                Fichas_iniciais-= quantidade
                print("NÃO FOI DESSA VEZ")
                print("Sua quantidade de fichas atual é {0}".format(Fichas_iniciais))
            else:
                print("Os dados foram {0} e {1} somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print('Você foi para a FASE POINT')
                point=dado_1+dado_2
                print("O seu Point é {0}".format(point))
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
        elif aposta == "Field":
            #print("Você está na fase C")
            if dado_1+dado_2==5 or dado_1+dado_2==6 or dado_1+dado_2==7 or dado_1+dado_2==8:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("NÃO FOI DESSA VEZ")
                Fichas_iniciais-=quantidade
                print(Fichas_iniciais)
            elif dado_1+dado_2==3 or dado_1+dado_2==4 or dado_1+dado_2==9 or dado_1+dado_2==10 or dado_1+dado_2==11:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABÉNS, VOCÊ GANHOU")
                Fichas_iniciais+=quantidade
                print(Fichas_iniciais)
            elif dado_1+dado_2==2:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABÉNS,VOCÊ GANHOU EM DOBRO")
                Fichas_iniciais+=2*quantidade
                print(Fichas_iniciais)
            else:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABÉNS, VOCÊ GANHOU 3x O VALOR!!!")
                Fichas_iniciais+=3*quantidade
                print(Fichas_iniciais)
        elif aposta == 'Any_craps':
            #print("Você está na fase C")
            if dado_1+dado_2==2 or dado_1+dado_2==3 or dado_1+dado_2==12:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABÉNS, VOCÊ GANHOU 7x O VALOR!!!")
                Fichas_iniciais+=7*quantidade
                print(Fichas_iniciais)
            else:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("NÃO FOI DESSA VEZ")
                Fichas_iniciais-=quantidade
                print(Fichas_iniciais)
        elif aposta == "Twelve":
            #print("Você está na fase C")
            if dado_1+dado_2 == 12:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("PARABÉNS, VOCÊ GANHOU 30x O VALOR!!!")
                Fichas_iniciais+=30*quantidade
                print(Fichas_iniciais)
            else:
                print("Os dados foram {0} e {1}, somando {2}".format(dado_1,dado_2,dado_1+dado_2))
                print("NÃO FOI DESSA VEZ")
                Fichas_iniciais-=quantidade
                print(Fichas_iniciais)
print("Você terminou o jogo com {0} fichas".format(Fichas_iniciais))